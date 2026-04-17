namespace SNUS_klk1_IndustrialProcessingSystem.Helpers;

public static class PayloadParser
{
    public static (int number, int threads) ParsePrime(string payload)
    {
        var parts = payload.Split(',');

        int number = 0;
        int threads = 1;

        foreach (var part in parts)
        {
            if (part.StartsWith("numbers:"))
            {
                var value = part.Replace("numbers:", "").Replace("_", "");
                number = int.Parse(value);
            }
            else if (part.StartsWith("threads:"))
            {
                threads = int.Parse(part.Replace("threads:", ""));
            }
        }

        threads = Math.Clamp(threads, 1, 8); // ограничение кол-ва нитей

        return (number, threads);
    }

    public static int ParseIO(string payload)
    {
        var value = payload.Replace("delay:", "").Replace("_", "");
        return int.Parse(value);
    }
}