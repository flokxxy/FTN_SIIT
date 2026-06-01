using SNUS_klk2_ChaoticCupid.Server.Models;

namespace SNUS_klk2_ChaoticCupid.Server.Services;

public class PersonStorage
{
    private readonly List<SinglePerson> _people = new();
    private readonly object _lock = new();

    public void AddOrUpdate(SinglePerson person)
    {
        //Adds a new user or updates an existing one by Username
        lock (_lock)
            // _lock is needed because different clients can access the data simultaneously, and on background Cupid
        {
            var existing = _people.FirstOrDefault(p => p.Username == person.Username);

            if (existing == null)
            {
                _people.Add(person);
            }
            else
            {
                existing.City = person.City;
                existing.Age = person.Age;
                existing.PhoneNumber = person.PhoneNumber;
                existing.ConnectionId = person.ConnectionId;
            }
        }
    }

    public List<SinglePerson> GetAll()
    //Returns a copy of the user list. Cupid uses it once per minute to select pairs for emails.
    {
        lock (_lock)
        {
            return _people.ToList();
        }
    }

    public SinglePerson? GetByUsername(string username)
    {
        lock (_lock)
        {
            return _people.FirstOrDefault(p => p.Username == username);
        }
    }

    public void ConfirmLetter(string username)
    {
        lock (_lock)
        {
            var person = _people.FirstOrDefault(p => p.Username == username);

            if (person != null)
            {
                person.HasUnconfirmedLetter = false;
            }
        }
    }

    public void BlockUser(string username, string blockedUsername)
    {
        lock (_lock)
        {
            var person = _people.FirstOrDefault(p => p.Username == username);

            if (person != null && !person.BlockedUsers.Contains(blockedUsername))
            {
                person.BlockedUsers.Add(blockedUsername);
            }
        }
    }

    public void RemoveByConnectionId(string connectionId)
    {
        lock (_lock)
        {
            _people.RemoveAll(p => p.ConnectionId == connectionId);
        }
    }

    public void SetHasUnconfirmedLetter(string username, bool value)
    {
        lock (_lock)
        {
            var person = _people.FirstOrDefault(p => p.Username == username);

            if (person != null)
            {
                person.HasUnconfirmedLetter = value;
            }
        }
    }
}
