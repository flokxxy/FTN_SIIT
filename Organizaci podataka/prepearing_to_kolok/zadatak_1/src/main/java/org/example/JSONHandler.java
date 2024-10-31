package org.example;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.Map;

public class JSONHandler {

    private static final String JSON_FILE = "departures.json";

    public void writeDeparturesToJSON(Map<String, List<Departure>> groupedDepartures) throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        mapper.enable(SerializationFeature.INDENT_OUTPUT);  // Beautify JSON output
        mapper.writeValue(new File(JSON_FILE), groupedDepartures);
    }
}
