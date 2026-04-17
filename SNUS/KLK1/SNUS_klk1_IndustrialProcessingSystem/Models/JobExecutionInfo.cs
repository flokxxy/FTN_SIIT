using SNUS_klk1_IndustrialProcessingSystem.Enums;
namespace SNUS_klk1_IndustrialProcessingSystem.Models;

public class JobExecutionInfo
//storage of execution history
{
    public Guid JobId { get; set; }
    public JobType Type { get; set; }
    public bool Success { get; set; }
    public double DurationMs { get; set; }
}