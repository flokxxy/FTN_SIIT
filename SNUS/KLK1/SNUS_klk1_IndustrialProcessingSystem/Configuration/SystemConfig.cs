namespace SNUS_klk1_IndustrialProcessingSystem.Configuration;

public class SystemConfig
{
    public int WorkerCount { get; set; }
    public int MaxQueueSize { get; set; }
    public List<ConfigJob> InitialJobs { get; set; } = new();
}