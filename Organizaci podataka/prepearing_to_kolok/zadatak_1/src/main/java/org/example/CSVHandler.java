package org.example;

import com.opencsv.CSVWriter;
import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvValidationException;

import java.io.FileWriter;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CSVHandler {

    private static final String CSV_FILE = "departures.csv";

    public void writeDeparturesToCSV(List<Departure> departures) throws IOException {
        try (CSVWriter writer = new CSVWriter(new FileWriter(CSV_FILE))) {
            String[] header = {"routeCode", "departurePlace", "arrivalPlace", "departureDate", "departureTime",
                    "arrivalTime", "platform", "ticketPrice", "ticketsSold"};
            writer.writeNext(header);

            for (Departure dep : departures) {
                writer.writeNext(new String[]{
                        dep.routeCode, dep.departurePlace, dep.arrivalPlace, dep.departureDate,
                        dep.departureTime, dep.arrivalTime, dep.platform,
                        String.valueOf(dep.ticketPrice), String.valueOf(dep.ticketsSold)
                });
            }
        }
    }

    public Map<String, List<Departure>> readDeparturesFromCSV() throws IOException, CsvValidationException {
        Map<String, List<Departure>> groupedDepartures = new HashMap<>();
        try (CSVReader csvReader = new CSVReader(new FileReader(CSV_FILE))) {
            csvReader.readNext();  // Пропуск заголовка
            String[] row;
            while ((row = csvReader.readNext()) != null) {
                Departure dep = new Departure(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                        Double.parseDouble(row[7]), Integer.parseInt(row[8]));

                groupedDepartures.computeIfAbsent(dep.routeCode, k -> new ArrayList<>()).add(dep);
            }
        }
        return groupedDepartures;
    }
}
