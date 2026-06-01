using Microsoft.AspNetCore.SignalR.Client;
using SNUS_klk2_ChaoticCupid.Client;
using SNUS_klk2_ChaoticCupid.Server.Contracts;
using SNUS_klk2_ChaoticCupid.Server.Hubs;
using SNUS_klk2_ChaoticCupid.Server.Models;
using SNUS_klk2_ChaoticCupid.Server.Services;

if (args.Length == 0)
{
    Console.WriteLine("Izaberite režim pokretanja:");
    Console.WriteLine("dotnet run -- server");
    Console.WriteLine("dotnet run -- client");
    return;
}

if (args[0].Equals("server", StringComparison.OrdinalIgnoreCase))
{
    await RunServer(args);
}
else if (args[0].Equals("client", StringComparison.OrdinalIgnoreCase))
{
    await RunClient();
}
else
{
    Console.WriteLine("Nepoznat režim.");
    Console.WriteLine("Koristite:");
    Console.WriteLine("dotnet run -- server");
    Console.WriteLine("dotnet run -- client");
}

static async Task RunServer(string[] args)
{
    var host = new HostBuilder()
        .ConfigureWebHost(webBuilder =>
        {
            webBuilder.UseKestrel();
            webBuilder.UseUrls("http://localhost:5000");

            webBuilder.ConfigureServices(services =>
            {
                services.AddSignalR();
                services.AddSingleton<PersonStorage>();
                services.AddSingleton<ICupidService, CupidService>();
                services.AddHostedService<CupidBackgroundService>();
            });

            webBuilder.Configure(app =>
            {
                app.UseRouting();
                app.UseEndpoints(endpoints =>
                {
                    endpoints.MapHub<CupidHub>("/cupidHub");
                });
            });
        })
        .Build();

    await host.StartAsync();

    Console.WriteLine("Server je pokrenut.");
    Console.WriteLine("SignalR Hub: http://localhost:5000/cupidHub");

    await host.WaitForShutdownAsync();
}

static async Task RunClient()
{
    Console.WriteLine("=== Haotični Kupidon ===");

    string username = InputHelper.ReadRequiredString("Unesite username: ");
    string city = InputHelper.ReadCity("Unesite grad: ");
    int age = InputHelper.ReadPositiveInt("Unesite godine (broj): ");
    string phoneNumber = InputHelper.ReadPhoneNumber("Unesite broj telefona (samo cifre): ");

    var connection = new HubConnectionBuilder()
        .WithUrl("http://localhost:5000/cupidHub")
        .WithAutomaticReconnect()
        .Build();

    connection.On<LoveLetter>("ReceiveLoveLetter", letter =>
    {
        Console.WriteLine();
        Console.WriteLine("==================================");
        Console.WriteLine("Stiglo je ljubavno pismo!");
        Console.WriteLine($"Od: {letter.FromUsername}");
        Console.WriteLine($"Grad: {letter.FromCity}");
        Console.WriteLine($"Godine: {letter.FromAge}");
        Console.WriteLine($"Poruka: {letter.Message}");

        if (!string.IsNullOrWhiteSpace(letter.FromPhoneNumber))
        {
            Console.WriteLine($"Telefon: {letter.FromPhoneNumber}");
        }
        Console.WriteLine("==================================");
        Console.WriteLine("Unesite /confirm da potvrdite prijem pisma.");
    });

    await connection.StartAsync();

    await connection.InvokeAsync(
        "InitSinglePerson",
        username,
        city,
        age,
        phoneNumber
    );

    Console.WriteLine("Uspešno ste prijavljeni.");
    Console.WriteLine("Komande:");
    Console.WriteLine("/confirm - potvrdi primljeno pismo");
    Console.WriteLine("/block username - blokiraj korisnika");

    while (true)
    {
        string? command = Console.ReadLine();

        if (string.IsNullOrWhiteSpace(command))
            continue;

        if (command.Equals("/confirm", StringComparison.OrdinalIgnoreCase))
        {
            await connection.InvokeAsync("ConfirmLetter", username);
            Console.WriteLine("Potvrdili ste prijem pisma.");
        }
        else if (command.StartsWith("/block ", StringComparison.OrdinalIgnoreCase))
        {
            string blockedUsername = command.Replace("/block ", "").Trim();

            if (string.IsNullOrWhiteSpace(blockedUsername))
            {
                Console.WriteLine("Morate uneti username za blokiranje.");
                continue;
            }

            await connection.InvokeAsync("BlockUser", username, blockedUsername);
            Console.WriteLine($"Blokirali ste korisnika: {blockedUsername}");
        }
        else
        {
            Console.WriteLine("Nepoznata komanda.");
        }
    }
}
