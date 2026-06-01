namespace SNUS_klk2_ChaoticCupid.Server.Contracts;

public interface ICupidService
{
    Task SendLoveLetters(CancellationToken cancellationToken);
}
