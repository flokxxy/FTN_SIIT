package org.example;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class ReaderCSV {

    // Метод для чтения данных о работах из CSV файла
    public static List<Work> readCSV(String filePath) throws IOException {
        List<Work> works = new ArrayList<>();
        BufferedReader reader = new BufferedReader(new FileReader(filePath));
        String line;
        while ((line = reader.readLine()) != null) {
            String[] values = line.split(",");
            if (values.length >= 5) {
                String JobTitle = values[0].trim();
                String JobType = values[1].trim();
                String companyN = values[2].trim();
                int time_work = Integer.parseInt(values[3].trim());
                double stavka = Double.parseDouble(values[4].trim());

                Work work = new Work(JobTitle, JobType, companyN, time_work, stavka);
                works.add(work);
            }
        }
        reader.close();
        return works;
    }

    // Метод для записи данных в CSV файл
    public static void writeCSV(String filePath, List<Work> works) throws IOException {
        FileWriter writer = new FileWriter(filePath);
        writer.append("JobTitle,JobType,CompanyName,TimeWorked,HourlyRate\n");
        for (Work work : works) {
            writer.append(String.format("%s,%s,%s,%d,%.2f\n",
                    work.getJobTitle(), work.getJobType(), work.getCompanyN(), work.getTime_work(), work.getInWork()));
        }
        writer.close();
    }

    // Метод для обработки работ и группировки по компаниям
    public static Map<String, Company> processWorks(List<Work> works) {
        Map<String, Company> companies = new HashMap<>();
        for (Work work : works) {
            Company company = companies.get(work.getCompanyN());
            if (company == null) {
                company = new Company(work.getCompanyN());
                companies.put(work.getCompanyN(), company);
            }
            company.addWork(work);
        }
        return companies;
    }

    // Метод для записи данных о компаниях в JSON
    public static void writeJSON(String filePath, Map<String, Company> companies) throws IOException {
        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.writeValue(new FileWriter(filePath), companies);
    }
}
