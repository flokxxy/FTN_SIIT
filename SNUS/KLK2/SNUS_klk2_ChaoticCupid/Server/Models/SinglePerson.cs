namespace SNUS_klk2_ChaoticCupid.Server.Models;

public class SinglePerson
{
    public string Username { get; set; } = string.Empty;
    public string City { get; set; } = string.Empty;
    public int Age { get; set; }
    public string PhoneNumber { get; set; } = string.Empty;

    public string ConnectionId { get; set; } = string.Empty;

    public bool HasUnconfirmedLetter { get; set; }

    public List<string> BlockedUsers { get; set; } = new();
}