using SNUS_klk1_IndustrialProcessingSystem.Models;
using SNUS_klk1_IndustrialProcessingSystem.Enums;
using SNUS_klk1_IndustrialProcessingSystem.Helpers;

namespace SNUS_klk1_IndustrialProcessingSystem.Services;

public class ProcessingSystem
{
    private readonly PriorityQueue<Job, int> _queue = new();
    private readonly SemaphoreSlim _signal = new(0);
    private readonly object _lock = new();

    private readonly int _maxQueueSize;
    
    private readonly HashSet<Guid> _pendingIds = new();
    private readonly HashSet<Guid> _completedIds = new();

    private readonly Dictionary<Guid, TaskCompletionSource<int>> _jobResults = new();
    private readonly Dictionary<Guid, Job> _allJobs = new();

    private readonly List<JobExecutionInfo> _history = new();
    private readonly ReportService _reportService;

    public event Action<Guid, int>? JobCompleted;
    public event Action<Guid, string>? JobFailed;

    public ProcessingSystem(int workerCount, int maxQueueSize)
    {
        _maxQueueSize = maxQueueSize; 
        _reportService = new ReportService(
            Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "Data", "reports")
        );

        Task.Run(ReportLoop);
    }
    
    public void StartWorkers(int workerCount)
    {
        for (int i = 0; i < workerCount; i++)
            Task.Run(WorkerLoop);
    }

    public JobHandle Submit(Job job)
    {
        var tcs = new TaskCompletionSource<int>(TaskCreationOptions.RunContinuationsAsynchronously);

        lock (_lock)
        {
            if (_pendingIds.Contains(job.Id) || _completedIds.Contains(job.Id))
                throw new InvalidOperationException($"Job {job.Id} already submitted or completed");

            if (_queue.Count >= _maxQueueSize)
                throw new InvalidOperationException($"Queue is full (max {_maxQueueSize})");

            _pendingIds.Add(job.Id);
            _jobResults[job.Id] = tcs;
            _allJobs[job.Id] = job;

            _queue.Enqueue(job, job.Priority);
        }

        _signal.Release();

        return new JobHandle
        {
            Id = job.Id,
            Result = tcs.Task
        };
    }

    public Job? GetJob(Guid id)
    {
        lock (_lock)
        {
            //return _allJobs.TryGetValue(id, out var job) ? job : null;
            return _allJobs.TryGetValue(id, out var job) ? job.Clone() : null;
        }
    }

    public IEnumerable<Job> GetTopJobs(int n)
    {
        lock (_lock)
        {
            return _queue.UnorderedItems
                .Select(x => x.Element)
                .OrderBy(j => j.Priority)
                .Take(n)
                .ToList();
        }
    }

    private async Task WorkerLoop()
    {
        while (true)
        {
            await _signal.WaitAsync();

            Job job;
            lock (_lock)
            {
                if (!_queue.TryDequeue(out job!, out _))
                    continue;
            }

            var start = DateTime.UtcNow;
            Console.WriteLine($"[Worker] Processing {job.Type} (Priority {job.Priority}) id={job.Id}");
            
            TaskCompletionSource<int>? tcs;
            bool success;
            int result = 0;
            string errorMessage = "";

            try
            {
                result = await ExecuteWithRetry(job);
                success = true;
            }
            catch (Exception ex)
            {
                success = false;
                errorMessage = ex.Message;
            }

            //var duration = (long)(DateTime.UtcNow - start).TotalMilliseconds;
            var duration = (DateTime.UtcNow - start).TotalMilliseconds;
            
            lock (_lock)
            {
                _history.Add(new JobExecutionInfo
                {
                    JobId = job.Id,
                    Type = job.Type,
                    Success = success,
                    DurationMs = duration
                });

                tcs = _jobResults.GetValueOrDefault(job.Id);
                _jobResults.Remove(job.Id);

                
                _pendingIds.Remove(job.Id);
                _completedIds.Add(job.Id);

                job.Status = success ? JobStatus.Completed : JobStatus.Failed;
            }

            
            if (success)
            {
                tcs?.SetResult(result);
                JobCompleted?.Invoke(job.Id, result);
                Console.WriteLine($"[Worker] Finished {job.Id} -> {result}");
            }
            else
            {
                tcs?.SetException(new Exception(errorMessage));
                JobFailed?.Invoke(job.Id, errorMessage);
                Console.WriteLine($"[Worker] Failed {job.Id}: {errorMessage}");
            }
        }
    }

    private async Task<int> ExecuteWithRetry(Job job)
    {
        const int maxAttempts = 3;
        job.Status = JobStatus.Running;

        for (int attempt = 1; attempt <= maxAttempts; attempt++)
        {
            job.RetryCount = attempt;
            Console.WriteLine($"[Retry] Job {job.Id} attempt {attempt}/{maxAttempts}");

            var processingTask = ProcessJob(job);
            var timeoutTask = Task.Delay(2000);

            var completed = await Task.WhenAny(processingTask, timeoutTask);

            if (completed == processingTask)
            {
                return await processingTask;
            }

            Console.WriteLine($"[Retry] Job {job.Id} timed out on attempt {attempt}");

            if (attempt == maxAttempts)
            {
                job.Status = JobStatus.Aborted;
                Console.WriteLine($"[Retry] Job {job.Id} ABORTED after {maxAttempts} attempts");
                throw new Exception($"Job aborted after {maxAttempts} failed attempts");
            }
        }

        throw new Exception("Unexpected error in ExecuteWithRetry");
    }

    private async Task<int> ProcessJob(Job job)
    {
        //метод решает как именно обработать джоб в зависимости от его типа
        switch (job.Type)
        {
            case JobType.IO:
                var delay = PayloadParser.ParseIO(job.Payload);
                await Task.Run(() => Thread.Sleep(delay));
                return Random.Shared.Next(0, 101);

            case JobType.Prime:
                var (number, threads) = PayloadParser.ParsePrime(job.Payload);
                return await Task.Run(() => CountPrimes(number, threads));

            default:
                throw new ArgumentException($"Unknown job type: {job.Type}");
        }
    }

    private async Task ReportLoop()
    {
        while (true)
        {
            await Task.Delay(TimeSpan.FromMinutes(1));

            List<JobExecutionInfo> snapshot;

            lock (_lock)
            {
                snapshot = _history.ToList();
            }

            _reportService.GenerateReport(snapshot);
            Console.WriteLine($"[Report] Generated at {DateTime.Now}");
        }
    }

    private int CountPrimes(int n, int threads)
    {
        int count = 0;
        var options = new ParallelOptions { MaxDegreeOfParallelism = threads };

        Parallel.For(2, n + 1, options, i =>
        {
            bool isPrime = true;
            for (int j = 2; j * j <= i; j++)
            {
                if (i % j == 0)
                {
                    isPrime = false;
                    break;
                }
            }

            if (isPrime)
                Interlocked.Increment(ref count);
        });

        return count;
    }
}