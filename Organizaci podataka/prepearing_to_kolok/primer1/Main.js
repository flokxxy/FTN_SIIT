package org.example;

import java.io.IOException;
import java.util.List;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        try {
            // Шаг 1: Генерация данных о работах
            List<Work> works = generateWorks();

            // Шаг 2: Запись данных в CSV файл
            String csvFilePath = "works.csv";
            ReaderCSV.writeCSV(csvFilePath, works);
            System.out.println("Data written to CSV file.");

            // Шаг 3: Чтение данных из CSV файла
            List<Work> readWorks = ReaderCSV.readCSV(csvFilePath);

            // Шаг 4: Обработка и группировка данных по компаниям
            Map<String, Company> companies = ReaderCSV.processWorks(readWorks);

            // Шаг 5: Запись данных о компаниях в JSON
            String jsonFilePath = "companies.json";
            ReaderCSV.writeJSON(jsonFilePath, companies);
            System.out.println("Data written to JSON file.");

        } catch (IOException e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }

    // Метод для создания тестовых данных
    private static List<Work> generateWorks() {
        List<Work> works = List.of(
                new Work("Repair", "Repair", "CompanyA", 10, 50),
                new Work("Maintenance", "Maintenance", "CompanyA", 5, 30),
                new Work("Repair", "Repair", "CompanyB", 8, 60),
                new Work("Cleaning", "Cleaning", "CompanyC", 15, 25),
                new Work("Repair", "Repair", "CompanyC", 12, 55)
        );
        return works;
    }
}
