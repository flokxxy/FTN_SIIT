using SNUS_klk1_IndustrialProcessingSystem.Enums;

namespace SNUS_klk1_IndustrialProcessingSystem.Models;

public class Job
{
    public Guid Id { get; set; }
    public JobType Type { get; set; }
    public string Payload { get; set; } = string.Empty;
    public int Priority { get; set; }

    public DateTime CreatedAt { get; set; } = DateTime.UtcNow; // время создание джоба
    public int RetryCount { get; set; } = 0; //счётчик текущей попытки
    public JobStatus Status { get; set; } = JobStatus.Pending; 
    //статус джоба, который меняется в процессе выполнения
    
    public Job Clone() => new Job
    {
        Id = this.Id,
        Type = this.Type,
        Payload = this.Payload,
        Priority = this.Priority,
        CreatedAt = this.CreatedAt,
        RetryCount = this.RetryCount,
        Status = this.Status
    };
}