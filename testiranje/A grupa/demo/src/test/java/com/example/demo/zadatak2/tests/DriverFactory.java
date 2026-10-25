package com.example.demo.zadatak2.tests;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.safari.SafariDriver;

import java.nio.file.Paths;
import java.util.Locale;
import java.util.concurrent.TimeUnit;

/**
 * Helper-класс для создания WebDriver.
 *
 * На Mac по умолчанию запускаем SafariDriver, потому что он уже есть в системе.
 * В NTP/Windows окружении можно запустить Edge:
 * -Dbrowser=edge
 */
public final class DriverFactory {

    private DriverFactory() {
    }

    /**
     * Создает browser driver на основе системного свойства -Dbrowser.
     * Если свойство не задано, выбирается браузер по операционной системе.
     */
    public static WebDriver createDriver() {
        String browser = System.getProperty("browser", defaultBrowser()).toLowerCase(Locale.ROOT);
        WebDriver driver;

        if ("edge".equals(browser)) {
            setDefaultEdgeDriverIfMissing();
            driver = new EdgeDriver();
        } else if ("safari".equals(browser)) {
            driver = new SafariDriver();
        } else {
            throw new IllegalArgumentException("Unsupported browser: " + browser);
        }

        driver.manage().timeouts().implicitlyWait(0, TimeUnit.SECONDS);
        driver.manage().window().maximize();
        return driver;
    }

    /**
     * Выбирает браузер по умолчанию.
     * Mac -> Safari, остальные системы -> Edge, потому что в проекте уже лежит msedgedriver.exe.
     */
    private static String defaultBrowser() {
        String osName = System.getProperty("os.name", "").toLowerCase(Locale.ROOT);
        return osName.contains("mac") ? "safari" : "edge";
    }

    /**
     * Если путь к Edge driver не задан вручную, берем msedgedriver.exe из корня проекта.
     */
    private static void setDefaultEdgeDriverIfMissing() {
        if (System.getProperty("webdriver.edge.driver") != null) {
            return;
        }

        String driverPath = Paths.get("msedgedriver.exe").toAbsolutePath().toString();
        System.setProperty("webdriver.edge.driver", driverPath);
    }
}
