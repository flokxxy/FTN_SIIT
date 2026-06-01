using System.Security.Cryptography;
using Microsoft.AspNetCore.SignalR;
using SNUS_klk2_ChaoticCupid.Server.Contracts;
using SNUS_klk2_ChaoticCupid.Server.Hubs;
using SNUS_klk2_ChaoticCupid.Server.Models;

namespace SNUS_klk2_ChaoticCupid.Server.Services;

public class CupidService : ICupidService
{
    private const string NotInterestedMessage = "Nisam zainteresovan/a za upoznavanje.";

    private readonly PersonStorage _storage;
    private readonly IHubContext<CupidHub> _hubContext;

    public CupidService(PersonStorage storage, IHubContext<CupidHub> hubContext)
    {
        _storage = storage;
        _hubContext = hubContext;
    }

    public async Task SendLoveLetters(CancellationToken cancellationToken)
    {
        var people = _storage.GetAll();

        foreach (var receiver in people)
        {
            if (receiver.HasUnconfirmedLetter)
                continue;

            var sender = FindBestMatch(receiver, people);

            if (sender == null)
                continue;

            var message = GetRandomMessage();

            var letter = new LoveLetter
            {
                FromUsername = sender.Username,
                FromCity = sender.City,
                FromAge = sender.Age,
                Message = message,
                FromPhoneNumber = message == NotInterestedMessage
                    ? null
                    : sender.PhoneNumber
            };

            await _hubContext.Clients
                .Client(receiver.ConnectionId)
                .SendAsync("ReceiveLoveLetter", letter, cancellationToken);

            Console.WriteLine($"Letter sent: {sender.Username} -> {receiver.Username}");

            _storage.SetHasUnconfirmedLetter(receiver.Username, true);
        }
    }

    private static SinglePerson? FindBestMatch(SinglePerson receiver, List<SinglePerson> people)
    {
        SinglePerson? bestCandidate = null;
        int bestScore = -1;

        foreach (var candidate in people)
        {
            if (candidate.Username == receiver.Username)
                continue;

            if (receiver.BlockedUsers.Contains(candidate.Username))
                continue;

            int score = CalculateScore(receiver, candidate);

            if (score > bestScore)
            {
                bestScore = score;
                bestCandidate = candidate;
            }
        }

        return bestCandidate;
    }

    private static int CalculateScore(SinglePerson receiver, SinglePerson candidate)
    {
        int score = 0;

        if (receiver.City.Equals(candidate.City, StringComparison.OrdinalIgnoreCase))
        {
            score += 30;
        }

        if (Math.Abs(receiver.Age - candidate.Age) <= 2)
        {
            score += 20;
        }

        score += RandomNumberGenerator.GetInt32(0, 101);

        return score;
    }

    private static string GetRandomMessage()
    {
        string[] messages =
        {
            "Radujem se našem susretu!",
            "Želim da se upoznamo.",
            NotInterestedMessage
        };

        int index = RandomNumberGenerator.GetInt32(0, messages.Length);

        return messages[index];
    }
}
