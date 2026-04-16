import allure
from selenium import webdriver
from pagescalculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест сложения на калькуляторе с задержкой")
@allure.description("Устанавливаем задержку 45 секунд, нажимаем 7 + 8 =, проверяем результат 15")
def test_calculator():
    driver = webdriver.Chrome()
    calculator = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calculator.open()

    with allure.step("Установить задержку 45 секунд"):
        calculator.set_delay("45")

    with allure.step("Нажать кнопки 7 + 8 ="):
        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")
        calculator.click_button("=")

    with allure.step("Получить результат и проверить его"):
        result = calculator.get_result()
        assert result == "15"

    driver.quit()
