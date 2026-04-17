using System.Xml.Linq;
using SNUS_klk1_IndustrialProcessingSystem.Models;

namespace SNUS_klk1_IndustrialProcessingSystem.Services;

public class ReportService
{
    //collecting task execution statistics and saving them to an XML file
    private readonly string _folder;
    private int _index = 0;

    public ReportService(string folder)
    {
        _folder = folder;
        Directory.CreateDirectory(_folder);
    }

    public void GenerateReport(List<JobExecutionInfo> history)
    {
        
        var report = history
            .GroupBy(x => x.Type)
            .Select(g => new
            {
                Type = g.Key,
                TotalCompleted = g.Count(x => x.Success),
                AvgTimeMs = g.Any(x => x.Success)
                    ? Math.Round(g.Where(x => x.Success).Average(x => x.DurationMs), 2)
                    : 0.0,
                Failed = g.Count(x => !x.Success)
            })
            .OrderBy(x => x.Type.ToString())
            .ToList();

        var xml = new XElement("Report",
            new XAttribute("GeneratedAt", DateTime.Now.ToString("o")),
            report.Select(r =>
                new XElement("JobType",
                    new XAttribute("Type", r.Type),
                    new XElement("TotalCompleted", r.TotalCompleted),
                    new XElement("AverageTimeMs", r.AvgTimeMs),
                    new XElement("Failed", r.Failed)
                )
            )
        );

        
        var filePath = Path.Combine(_folder, $"report_{_index}.xml");
        xml.Save(filePath);

        Console.WriteLine($"[Report] Saved to {filePath}");

        _index = (_index + 1) % 10;
    }
}