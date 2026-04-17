using SNUS_klk1_IndustrialProcessingSystem.Configuration;
using SNUS_klk1_IndustrialProcessingSystem.Models;
using SNUS_klk1_IndustrialProcessingSystem.Enums;
using SNUS_klk1_IndustrialProcessingSystem.Services;

class Program
{
    static async Task Main()
    {
        var path = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "Data", "SystemConfig.xml");
        var config = ConfigLoader.Load(path);
        Console.WriteLine($"Config loaded: Workers={config.WorkerCount}, MaxQueue={config.MaxQueueSize}, Jobs={config.InitialJobs.Count}");


        var system = new ProcessingSystem(config.WorkerCount, config.MaxQueueSize);

        var logPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "Data", "logs.txt");
        var logger = new LogService(logPath);

        system.JobCompleted += async (id, result) =>
        {
            var message = $"[{DateTime.Now}] [COMPLETED] {id}, {result}";
            await logger.WriteAsync(message);
        };

        system.JobFailed += async (id, error) =>
        {
            string status = error.Contains("aborted", StringComparison.OrdinalIgnoreCase)
                ? "ABORT" : "FAILED";
            var message = $"[{DateTime.Now}] [{status}] {id}, {error}";
            await logger.WriteAsync(message);
        };

        foreach (var jobConfig in config.InitialJobs)
        {
            try
            {
                var job = new Job
                {
                    Id = jobConfig.Id,
                    Type = Enum.Parse<JobType>(jobConfig.Type),
                    Payload = jobConfig.Payload,
                    Priority = jobConfig.Priority
                };

                Console.WriteLine($"Submitting initial job: {job.Id} [{job.Type}] priority={job.Priority}");
                system.Submit(job);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Failed to submit initial job: {ex.Message}");
            }
        }

        var topJobs = system.GetTopJobs(3);
        Console.WriteLine("\nTOP 3 JOBS:");
        foreach (var job in topJobs)
            Console.WriteLine($"  {job.Id} [{job.Type}] priority={job.Priority}");
        Console.WriteLine();
        
        system.StartWorkers(config.WorkerCount);

        var cts = new CancellationTokenSource();
        
        var producerTasks = Enumerable.Range(0, config.WorkerCount).Select(i => Task.Run(async () =>
        {
            var rng = new Random();
            Console.WriteLine($"Producer thread {i} started");

            while (!cts.Token.IsCancellationRequested)
            {
                try
                {
                    var isIO = rng.Next(2) == 0;
                    var job = new Job
                    {
                        Id = Guid.NewGuid(),
                        Type = isIO ? JobType.IO : JobType.Prime,
                        Payload = isIO
                            ? $"delay:{rng.Next(100, 2500)}"
                            : $"numbers:{rng.Next(100, 5000)},threads:{rng.Next(1, 8)}",
                        Priority = rng.Next(1, 10)
                    };

                    system.Submit(job);
                    Console.WriteLine($"[Producer {i}] Submitted {job.Type} priority={job.Priority}");
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"[Producer {i}] Submit rejected: {ex.Message}");
                }

                await Task.Delay(rng.Next(300, 1200), cts.Token).ContinueWith(_ => { });
            }
        }, cts.Token)).ToList();

        Console.WriteLine("System running. Press Enter to stop...");
        Console.ReadLine();

        cts.Cancel();
        await Task.WhenAll(producerTasks);

        Console.WriteLine("All producers stopped. Goodbye.");
    }
}