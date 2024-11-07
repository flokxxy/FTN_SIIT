package org.example;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.util.ArrayList;
import java.util.List;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args){
        try{
            List<Work> works = ReaderCSV.readCSV("works.csv");
            Map<String,Company> companies = ReaderCSV.processWorks(works);

            //сорт по ср доходу
            List<Company> sortComp = new ArrayList<>(companies.values());
            sortComp.sort(Comparator.comparingDouble(Company::getSrHours).reversed());
            //преобр в json
            ObjectsMapper objectsMapper = new ObjectMapper();
            String jsom = objectsMapper.writeValueAsString(sortComp);

            System.out.printf(json);

        }
        catch (IOException e){
            e.printStackTrace();
        }
    }
}
