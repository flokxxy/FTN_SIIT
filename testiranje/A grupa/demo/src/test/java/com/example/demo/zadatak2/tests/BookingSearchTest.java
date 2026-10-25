package com.example.demo.zadatak2.tests;

import com.example.demo.zadatak2.pages.HomePage;
import com.example.demo.zadatak2.pages.ResultsPage;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.WebDriver;

import java.time.LocalDate;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * E2E тест полного korisnickog scenarija:
 * открываем booking.com, задаем параметры поиска и проверяем страницу результатов.
 */
class BookingSearchTest {

    private static final String DESTINATION = "Zlatibor";
    private static final int ADULTS = 1;
    private static final int CHILDREN = 2;
    private static final int ROOMS = 1;
    private static final int NIGHTS = 5;

    private WebDriver driver;

    /**
     * BeforeEach запускается перед каждым тестом.
     * Здесь создаем браузер, чтобы каждый тест стартовал с чистого состояния.
     */
    @BeforeEach
    void setUp() {
        driver = DriverFactory.createDriver();
    }

    /**
     * AfterEach закрывает браузер после теста.
     * Это важно, иначе после нескольких запусков останется много открытых окон.
     */
    @AfterEach
    void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    /**
     * Сам тест должен быть коротким:
     * 1. Подготавливаем данные.
     * 2. Через HomePage выполняем поиск.
     * 3. Через ResultsPage проверяем результат.
     */
    @Test
    void shouldFindZlatiborOffersForOneAdultAndTwoChildren() {
        // В PDF стоят даты 15.01.2024-20.01.2024, но сейчас они уже прошли.
        // Для реального запуска используем будущие даты с тем же интервалом: 5 ночей.
        LocalDate checkIn = LocalDate.of(2026, 7, 15);
        LocalDate checkOut = checkIn.plusDays(NIGHTS);

        HomePage homePage = new HomePage(driver);
        homePage.open();
        homePage.search(DESTINATION, checkIn, checkOut, ADULTS, CHILDREN, List.of(12, 15), ROOMS);

        ResultsPage resultsPage = new ResultsPage(driver);

        assertTrue(resultsPage.isLoaded(), "Search results page should be loaded.");
        assertTrue(resultsPage.allOffersContainLocation(DESTINATION),
                "All offers on the first page should be located in Zlatibor.");
        assertTrue(resultsPage.allOffersContainStayCriteria(NIGHTS, ADULTS, CHILDREN),
                "Results should contain criteria: 5 nights, 1 adult and 2 children.");
    }
}
