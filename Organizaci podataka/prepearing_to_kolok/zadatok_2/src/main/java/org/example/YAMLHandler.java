package org.example;

import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.DumperOptions.FlowStyle;

import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class YAMLHandler {

    private static final String YAML_FILE = "analysis_results.yaml";

    public void writeResultsToYAML(String mostFrequentRoute, String longestRoute, String mostProfitableRoute) throws IOException {
        Map<String, String> results = new HashMap<>();
        results.put("Most Frequent Route", mostFrequentRoute);
        results.put("Longest Route", longestRoute);
        results.put("Most Profitable Route", mostProfitableRoute);

        DumperOptions options = new DumperOptions();
        options.setDefaultFlowStyle(FlowStyle.BLOCK);
        Yaml yaml = new Yaml(options);

        try (FileWriter writer = new FileWriter(YAML_FILE)) {
            yaml.dump(results, writer);
        }
    }
}
