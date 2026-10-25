package com.example.demo.zadatak2.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.LocalDate;
import java.util.List;

/**
 * Page Object для начальной страницы booking.com.
 *
 * В Page Object мы прячем все Selenium-действия со страницей:
 * ввод destination, выбор дат, настройку количества гостей и запуск поиска.
 * Благодаря этому сам тест остается коротким и читабельным.
 */
public class HomePage {

    private static final String BASE_URL = "https://www.booking.com/?lang=en-us";

    private final WebDriver driver;
    private final WebDriverWait wait;

    private final By destinationInput = By.cssSelector("input[name='ss']");
    private final By searchButton = By.cssSelector("button[type='submit']");
    private final By occupancyButton = By.cssSelector("[data-testid='occupancy-config']");

    public HomePage(WebDriver driver) {
        this.driver = driver;
        // Explicit wait ждет конкретное состояние элемента.d
        // Это лучше, чем Thread.sleep(), потому что тест продолжит работу сразу,
        // когда элемент станет доступен, и не будет ждать лишнее время.
        this.wait = new WebDriverWait(driver, 20);
    }

    /**
     * Открывает booking.com и ждет, пока появится поле destination.
     * Если появится cookie popup, закрываем его, чтобы он не перекрывал форму.
     */
    public void open() {
        driver.get(BASE_URL);
        acceptCookiesIfVisible();
        wait.until(ExpectedConditions.visibilityOfElementLocated(destinationInput));
    }

    /**
     * Главный публичный метод страницы.
     * Тест вызывает только его, а все мелкие Selenium-шаги остаются внутри Page Object.
     */
    public void search(String destination, LocalDate checkIn, LocalDate checkOut,
                       int adults, int children, List<Integer> childrenAges, int rooms) {
        enterDestination(destination);
        selectDateRange(checkIn, checkOut);
        setOccupancy(adults, children, childrenAges, rooms);
        wait.until(ExpectedConditions.elementToBeClickable(searchButton)).click();
    }

    /**
     * Находит поле "Where are you going?", очищает его и вводит город.
     * Keys.ENTER подтверждает вариант из автокомплита, если он появился.
     */
    private void enterDestination(String destination) {
        WebElement input = wait.until(ExpectedConditions.elementToBeClickable(destinationInput));
        input.clear();
        input.sendKeys(destination);
        input.sendKeys(Keys.ENTER);
    }

    /**
     * Открывает календарь и выбирает дату заезда и дату выезда.
     * Передаем LocalDate, потому что его строковый формат yyyy-MM-dd совпадает
     * с data-date атрибутом, который booking.com обычно ставит на дни календаря.
     */
    private void selectDateRange(LocalDate checkIn, LocalDate checkOut) {
        clickFirstAvailable(
                By.cssSelector("[data-testid='date-display-field-start']"),
                By.cssSelector("[data-testid='searchbox-dates-container']"),
                By.cssSelector("button[data-testid='date-display-field-start']")
        );

        selectDate(checkIn);
        selectDate(checkOut);
    }

    /**
     * Ищет конкретный день в календаре.
     * Если день не виден в текущем месяце, нажимает "Next month" и пробует снова.
     * Ограничение 24 месяца защищает тест от бесконечного цикла.
     */
    private void selectDate(LocalDate date) {
        By dateCell = By.cssSelector("[data-date='" + date + "']");

        for (int i = 0; i < 24; i++) {
            List<WebElement> cells = driver.findElements(dateCell);
            if (!cells.isEmpty()) {
                cells.get(0).click();
                return;
            }

            clickFirstAvailable(
                    By.cssSelector("[data-testid='calendar-navigation-next']"),
                    By.cssSelector("button[aria-label='Next month']")
            );
        }

        throw new NoSuchElementException("Date was not found in date picker: " + date);
    }

    /**
     * Открывает блок с количеством гостей и настраивает adults, children и rooms.
     * В booking.com стандартные значения обычно: 2 взрослых, 0 детей, 1 комната.
     */
    private void setOccupancy(int adults, int children, List<Integer> childrenAges, int rooms) {
        wait.until(ExpectedConditions.elementToBeClickable(occupancyButton)).click();

        setCounter("Adults", adults, 2);
        setCounter("Children", children, 0);
        setCounter("Rooms", rooms, 1);
        setChildrenAges(childrenAges);
    }

    /**
     * Универсальная настройка счетчика.
     * Например, если взрослых нужно 1, а стандартно их 2, difference = -1,
     * значит один раз нажимаем Decrease.
     */
    private void setCounter(String label, int expectedValue, int defaultValue) {
        int difference = expectedValue - defaultValue;
        String action = difference > 0 ? "Increase" : "Decrease";

        for (int i = 0; i < Math.abs(difference); i++) {
            clickCounterButton(action, label);
        }
    }

    /**
     * Нажимает кнопку Increase/Decrease для нужного счетчика.
     * Здесь несколько локаторов, потому что HTML booking.com может немного меняться.
     */
    private void clickCounterButton(String action, String label) {
        clickFirstAvailable(
                By.xpath("//button[contains(@aria-label,'" + action + " number of " + label + "')]"),
                By.xpath("//label[contains(.,'" + label + "')]/ancestor::*[self::div or self::li][1]//button[contains(@aria-label,'" + action + "')]"),
                By.xpath("//*[contains(.,'" + label + "')]/ancestor::*[self::div or self::li][1]//button[contains(@aria-label,'" + action + "')]")
        );
    }

    /**
     * После добавления детей booking.com показывает select поля для возраста.
     * Select - стандартный Selenium-класс для работы с HTML <select>.
     */
    private void setChildrenAges(List<Integer> childrenAges) {
        List<WebElement> ageSelects = wait.until(ExpectedConditions.numberOfElementsToBeMoreThan(By.cssSelector("select[name='age']"), 0));

        for (int i = 0; i < childrenAges.size(); i++) {
            Select ageSelect = new Select(ageSelects.get(i));
            ageSelect.selectByValue(String.valueOf(childrenAges.get(i)));
        }
    }

    /**
     * Cookie popup может появиться, а может не появиться.
     * Поэтому используем короткий wait и игнорируем TimeoutException.
     */
    private void acceptCookiesIfVisible() {
        clickIfVisible(By.cssSelector("button[id='onetrust-accept-btn-handler']"));
        clickIfVisible(By.xpath("//button[contains(., 'Accept')]"));
    }

    /**
     * Пробует несколько локаторов и кликает первый найденный.
     * Это полезно для внешних сайтов: у них часто меняются data-testid или aria-label.
     */
    private void clickFirstAvailable(By... locators) {
        for (By locator : locators) {
            try {
                wait.until(ExpectedConditions.elementToBeClickable(locator)).click();
                return;
            } catch (TimeoutException ignored) {
            }
        }

        throw new NoSuchElementException("None of the locators were clickable.");
    }

    /**
     * Безопасный клик для необязательных элементов.
     * Если элемент не появился за 3 секунды, тест просто продолжает работу.
     */
    private void clickIfVisible(By locator) {
        try {
            new WebDriverWait(driver, 3).until(ExpectedConditions.elementToBeClickable(locator)).click();
        } catch (TimeoutException ignored) {
        }
    }
}
