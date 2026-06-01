namespace SNUS_klk2_ChaoticCupid.Client;

public class InputHelper
{
    public static string ReadRequiredString(string message)
    {
        while (true)
        {
            Console.Write(message);
            string? input = Console.ReadLine();

            if (!string.IsNullOrWhiteSpace(input))
            {
                return input.Trim();
            }

            Console.WriteLine("Polje ne sme biti prazno.");
        }
    }

    public static string ReadCity(string message)
    {
        while (true)
        {
            string city = ReadRequiredString(message);

            if (city.All(char.IsDigit))
            {
                Console.WriteLine("Grad ne moze biti samo broj.");
                continue;
            }

            if (city.Any(char.IsDigit))
            {
                Console.WriteLine("Grad ne sme da sadrzi cifre.");
                continue;
            }

            return city;
        }
    }

    public static int ReadPositiveInt(string message)
    {
        while (true)
        {
            Console.Write(message);
            string? input = Console.ReadLine();

            if (!int.TryParse(input, out int number))
            {
                Console.WriteLine("Morate uneti broj.");
                continue;
            }

            if (number <= 0)
            {
                Console.WriteLine("Broj mora biti pozitivan.");
                continue;
            }

            return number;
        }
    }

    public static string ReadPhoneNumber(string message)
    {
        while (true)
        {
            Console.Write(message);
            string? input = Console.ReadLine();

            if (string.IsNullOrWhiteSpace(input))
            {
                Console.WriteLine("Polje ne sme biti prazno.");
                continue;
            }

            string phoneNumber = input.Trim();

            if (phoneNumber.StartsWith("-"))
            {
                Console.WriteLine("Broj telefona ne sme biti negativan.");
                continue;
            }

            if (!phoneNumber.All(char.IsDigit))
            {
                Console.WriteLine("Broj telefona sme da sadrži samo cifre.");
                continue;
            }

            return phoneNumber;
        }
    }
}
