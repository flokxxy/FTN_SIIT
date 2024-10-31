package org.example;

import com.opencsv.exceptions.CsvValidationException;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        List<Departure> departures = generateDepartures();
        CSVHandler csvHandler = new CSVHandler();
        JSONHandler jsonHandler = new JSONHandler();

        try {
            // Step 1: Write data to CSV
            csvHandler.writeDeparturesToCSV(departures);

            // Step 2: Read data from CSV and group by route
            Map<String, List<Departure>> groupedDepartures = csvHandler.readDeparturesFromCSV();

            // Step 3: Write grouped data to JSON
            jsonHandler.writeDeparturesToJSON(groupedDepartures);

            System.out.println("Data successfully written to CSV and JSON files.");
        } catch (IOException | CsvValidationException e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }

    private static List<Departure> generateDepartures() {
        List<Departure> departures = new ArrayList<>();
        departures.add(new Departure("R001", "Belgrade", "Novi Sad", "2024-11-01", "08:00", "09:30", "1", 500, 30));
        departures.add(new Departure("R001", "Belgrade", "Novi Sad", "2024-11-01", "12:00", "13:30", "2", 500, 25));
        departures.add(new Departure("R002", "Novi Sad", "Subotica", "2024-11-01", "09:00", "10:30", "1", 400, 20));
        departures.add(new Departure("R002", "Novi Sad", "Subotica", "2024-11-01", "14:00", "15:30", "3", 400, 18));
        departures.add(new Departure("R003", "Belgrade", "Kragujevac", "2024-11-01", "07:30", "10:00", "5", 600, 35));
        departures.add(new Departure("R003", "Belgrade", "Kragujevac", "2024-11-01", "15:00", "17:30", "6", 600, 40));
        departures.add(new Departure("R004", "Kragujevac", "Nis", "2024-11-01", "09:30", "12:30", "4", 700, 15));
        departures.add(new Departure("R004", "Kragujevac", "Nis", "2024-11-01", "13:30", "16:30", "4", 700, 22));
        departures.add(new Departure("R005", "Nis", "Belgrade", "2024-11-01", "10:00", "14:00", "7", 800, 28));
        departures.add(new Departure("R005", "Nis", "Belgrade", "2024-11-01", "18:00", "22:00", "7", 800, 32));
        return departures;
    }
}
