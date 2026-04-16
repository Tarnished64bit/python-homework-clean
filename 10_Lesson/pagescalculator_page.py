from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Page Object для страницы калькулятора с задержкой.
    """

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        :param driver: WebDriver (экземпляр браузера)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> "CalculatorPage":
        """
        Открывает страницу калькулятора в браузере.

        :return: Экземпляр CalculatorPage для цепочки вызовов
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        return self

    def set_delay(self, seconds: str) -> "CalculatorPage":
        """
        Устанавливает задержку перед вычислением.

        :param seconds: Значение задержки (строка)
        :return: Экземпляр CalculatorPage для цепочки вызовов
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(seconds)
        return self

    def click_button(self, button_text: str) -> "CalculatorPage":
        """
        Нажимает кнопку на калькуляторе по её тексту.

        :param button_text: Текст на кнопке ("7", "+", "=", "8")
        :return: Экземпляр CalculatorPage для цепочки вызовов
        """
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']"
        )
        button.click()
        return self

    def get_result(self) -> str:
        """
        Ожидает появления результата "15" на экране калькулятора и возвращает его.

        :return: Текст результата
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result.text
