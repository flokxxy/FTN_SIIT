namespace SNUS_klk1_IndustrialProcessingSystem.Services;

public class LogService
{
    //writing logs to a file
    private readonly string _filePath;
    private readonly SemaphoreSlim _lock = new(1, 1);

    public LogService(string filePath)
    {
        _filePath = filePath;
    }

    public async Task WriteAsync(string message)
    {
        await _lock.WaitAsync();
        try
        {
            await File.AppendAllTextAsync(_filePath, message + Environment.NewLine);
        }
        finally
        {
            _lock.Release();
        }
    }
}