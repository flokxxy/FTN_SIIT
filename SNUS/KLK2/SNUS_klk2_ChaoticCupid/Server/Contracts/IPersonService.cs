namespace SNUS_klk2_ChaoticCupid.Server.Contracts;

public interface IPersonService
{
    Task InitSinglePerson(string username, string city, int age, string phoneNumber);
    Task ConfirmLetter(string username);
    Task BlockUser(string username, string blockedUsername);
}
