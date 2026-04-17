namespace SNUS_klk1_IndustrialProcessingSystem.Models;

public class JobHandle
{
    //returns the result of the work after submt
    public Guid Id { get; set; }
    public Task<int> Result { get; set; } = Task.FromResult(0);
}