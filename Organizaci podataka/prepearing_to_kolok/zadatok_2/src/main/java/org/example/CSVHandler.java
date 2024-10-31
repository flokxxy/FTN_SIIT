package org.example;

import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvValidationException;

import java.io.FileReader;
import java.io.IOException;
import java.time.Duration;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class CSVHandler {

    private static final String CSV_FILE = "departures.csv";

    // Чтение данных из CSV
    public List<Departure> readDeparturesFromCSV() throws IOException, CsvValidationException {
        List<Departure> departures = new ArrayList<>();
        try (CSVReader csvReader = new CSVReader(new FileReader(CSV_FILE))) {
            csvReader.readNext();  // Пропуск заголовка
            String[] row;
            while ((row = csvReader.readNext()) != null) {
                departures.add(new Departure(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                        Double.parseDouble(row[7]), Integer.parseInt(row[8])));
            }
        }
        return departures;
    }

    // Находит маршрут с наибольшим количеством рейсов
    public String findMostFrequentRoute(List<Departure> departures) {
        Map<String, Integer> routeCount = new HashMap<>();
        for (Departure dep : departures) {
            routeCount.put(dep.routeCode, routeCount.getOrDefault(dep.routeCode, 0) + 1);
        }
        return Collections.max(routeCount.entrySet(), Map.Entry.comparingByValue()).getKey();
    }

    // Находит маршрут с наибольшим временем в пути
    public String findLongestRoute(List<Departure> departures) {
        Map<String, Long> routeDuration = new HashMap<>();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm");

        for (Departure dep : departures) {
            LocalTime departureTime = LocalTime.parse(dep.departureTime, formatter);
            LocalTime arrivalTime = LocalTime.parse(dep.arrivalTime, formatter);
            long duration = Duration.between(departureTime, arrivalTime).toMinutes();
            routeDuration.put(dep.routeCode, routeDuration.getOrDefault(dep.routeCode, 0L) + duration);
        }
        return Collections.max(routeDuration.entrySet(), Map.Entry.comparingByValue()).getKey();
    }

    // Находит самый прибыльный маршрут
    public String findMostProfitableRoute(List<Departure> departures) {
        Map<String, Double> routeRevenue = new HashMap<>();
        for (Departure dep : departures) {
            double revenue = dep.ticketPrice * dep.ticketsSold;
            routeRevenue.put(dep.routeCode, routeRevenue.getOrDefault(dep.routeCode, 0.0) + revenue);
        }
        return Collections.max(routeRevenue.entrySet(), Map.Entry.comparingByValue()).getKey();
    }
}
