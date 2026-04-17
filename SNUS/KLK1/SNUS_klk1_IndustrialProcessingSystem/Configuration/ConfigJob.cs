namespace SNUS_klk1_IndustrialProcessingSystem.Configuration;

public class ConfigJob
{
    public Guid Id { get; set; }
    public string Type { get; set; } = string.Empty;
    public string Payload { get; set; } = string.Empty;
    public int Priority { get; set; }
}