using SNUS_klk2_ChaoticCupid.Server.Contracts;

namespace SNUS_klk2_ChaoticCupid.Server.Services;

public class CupidBackgroundService : BackgroundService
{
    private readonly ICupidService _cupidService;

    public CupidBackgroundService(ICupidService cupidService)
    {
        _cupidService = cupidService;
    }

    //send in 1 min
    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            await Task.Delay(TimeSpan.FromMinutes(1), stoppingToken);
            await _cupidService.SendLoveLetters(stoppingToken);
        }
    }
}
