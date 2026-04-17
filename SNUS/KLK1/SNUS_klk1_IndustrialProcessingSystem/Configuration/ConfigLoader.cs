using System.Xml.Linq;

namespace SNUS_klk1_IndustrialProcessingSystem.Configuration;

public static class ConfigLoader
{
    public static SystemConfig Load(string path)
    {
        var doc = XDocument.Load(path);
        var root = doc.Element("SystemConfig")
                   ?? throw new Exception("Invalid config");

        var config = new SystemConfig
        {
            WorkerCount = int.Parse(root.Element("WorkerCount")!.Value),
            MaxQueueSize = int.Parse(root.Element("MaxQueueSize")!.Value),
            InitialJobs = root.Element("Jobs")!
                .Elements("Job")
                .Select(x => new ConfigJob
                {
                    Id = Guid.NewGuid(), // 👈 важно! в XML нет Id
                    Type = x.Attribute("Type")!.Value,
                    Payload = x.Attribute("Payload")!.Value,
                    Priority = int.Parse(x.Attribute("Priority")!.Value)
                })
                .ToList()
        };

        return config;
    }

}