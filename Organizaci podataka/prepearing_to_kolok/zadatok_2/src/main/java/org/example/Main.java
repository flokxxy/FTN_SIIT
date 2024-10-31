package org.example;

import com.opencsv.exceptions.CsvValidationException;

import java.io.IOException;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        CSVHandler csvHandler = new CSVHandler();
        YAMLHandler yamlHandler = new YAMLHandler();

        try {
            // Чтение данных из CSV
            List<Departure> departures = csvHandler.readDeparturesFromCSV();

            // Анализ данных
            String mostFrequentRoute = csvHandler.findMostFrequentRoute(departures);
            String longestRoute = csvHandler.findLongestRoute(departures);
            String mostProfitableRoute = csvHandler.findMostProfitableRoute(departures);

            // Запись результатов в YAML
            yamlHandler.writeResultsToYAML(mostFrequentRoute, longestRoute, mostProfitableRoute);

            System.out.println("Analysis completed and results written to YAML file.");

        } catch (IOException | CsvValidationException e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}
