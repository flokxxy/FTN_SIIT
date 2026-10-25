package com.example.demo.zadatak2.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.List;
import java.util.Locale;
import java.util.stream.Collectors;

/**
 * Page Object для страницы результатов поиска.
 *
 * Здесь находятся только проверки и действия, которые относятся к странице
 * результатов: ожидание загрузки карточек и проверка текста предложений.
 */
public class ResultsPage {

    private final WebDriver driver;
    private final WebDriverWait wait;

    private final By propertyCards = By.cssSelector("[data-testid='property-card']");

    public ResultsPage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, 30);
    }

    /**
     * Проверяет, что страница результатов действительно загрузилась.
     * Достаточно увидеть URL searchresults или хотя бы одну карточку property-card.
     */
    public boolean isLoaded() {
        wait.until(ExpectedConditions.or(
                ExpectedConditions.urlContains("searchresults"),
                ExpectedConditions.visibilityOfElementLocated(propertyCards)
        ));
        return !getOffers().isEmpty();
    }

    /**
     * Возвращает карточки смештаја/отелей на первой странице результатов.
     */
    public List<WebElement> getOffers() {
        return driver.findElements(propertyCards);
    }

    /**
     * Преобразует карточки в обычный текст.
     * Так удобнее делать проверки через contains().
     */
    public List<String> getOfferTexts() {
        return getOffers().stream()
                .map(WebElement::getText)
                .collect(Collectors.toList());
    }

    /**
     * Проверяет, что каждая карточка на первой странице содержит нужную локацию.
     * Locale.ROOT нужен, чтобы lower-case работал предсказуемо независимо от языка ОС.
     */
    public boolean allOffersContainLocation(String location) {
        String expectedLocation = location.toLowerCase(Locale.ROOT);
        return getOfferTexts().stream()
                .allMatch(text -> text.toLowerCase(Locale.ROOT).contains(expectedLocation));
    }

    /**
     * Проверяет критерии проживания: количество ночей, взрослых и детей.
     * Эти данные booking.com иногда показывает не в каждой карточке отдельно,
     * поэтому проверяем текст всей страницы результатов.
     */
    public boolean allOffersContainStayCriteria(int nights, int adults, int children) {
        String pageText = driver.findElement(By.tagName("body")).getText().toLowerCase(Locale.ROOT);
        String expectedNights = nights + " nights";
        String expectedAdults = adults + " adult";
        String expectedChildren = children + " children";

        return pageText.contains(expectedNights)
                && pageText.contains(expectedAdults)
                && pageText.contains(expectedChildren);
    }
}
