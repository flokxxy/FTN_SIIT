namespace SNUS_klk2_ChaoticCupid.Server.Models;

public class LoveLetter
{
    public string FromUsername { get; set; } = string.Empty;
    public string FromCity { get; set; } = string.Empty;
    public int FromAge { get; set; }
    public string? FromPhoneNumber { get; set; }

    public string Message { get; set; } = string.Empty;
}