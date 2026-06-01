using SNUS_klk2_ChaoticCupid.Server.Models;
using SNUS_klk2_ChaoticCupid.Server.Services;
using Microsoft.AspNetCore.SignalR;
using SNUS_klk2_ChaoticCupid.Server.Contracts;

namespace SNUS_klk2_ChaoticCupid.Server.Hubs;

public class CupidHub : Hub, IPersonService
{
    private readonly PersonStorage _storage;

    public CupidHub(PersonStorage storage)
    {
        _storage = storage;
    }

    //registration client
    public Task InitSinglePerson(string username, string city, int age, string phoneNumber)
    {
        ValidateSinglePerson(username, city, age, phoneNumber);

        var person = new SinglePerson
        {
            Username = username,
            City = city,
            Age = age,
            PhoneNumber = phoneNumber,
            ConnectionId = Context.ConnectionId
        };

        _storage.AddOrUpdate(person);

        Console.WriteLine($"Registered: {username}, {city}, {age}");

        return Task.CompletedTask;
    }

    public Task ConfirmLetter(string username)
    {
        _storage.ConfirmLetter(username);

        Console.WriteLine($"{username} confirmed letter.");

        return Task.CompletedTask;
    }

    public Task BlockUser(string username, string blockedUsername)
    {
        _storage.BlockUser(username, blockedUsername);

        Console.WriteLine($"{username} blocked {blockedUsername}.");

        return Task.CompletedTask;
    }

    public override Task OnDisconnectedAsync(Exception? exception)
    {
        _storage.RemoveByConnectionId(Context.ConnectionId);
        return base.OnDisconnectedAsync(exception);
    }

    private static void ValidateSinglePerson(string username, string city, int age, string phoneNumber)
    {
        if (string.IsNullOrWhiteSpace(username))
            throw new HubException("Username ne sme biti prazan.");

        if (string.IsNullOrWhiteSpace(city))
            throw new HubException("Grad ne sme biti prazan.");

        if (city.Any(char.IsDigit))
            throw new HubException("Grad ne sme da sadrzi cifre.");

        if (age <= 0)
            throw new HubException("Godine moraju biti pozitivan broj.");

        if (string.IsNullOrWhiteSpace(phoneNumber))
            throw new HubException("Broj telefona ne sme biti prazan.");

        if (!phoneNumber.All(char.IsDigit))
            throw new HubException("Broj telefona sme da sadrži samo cifre.");
    }
}
