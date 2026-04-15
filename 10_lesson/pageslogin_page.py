from selenium.webdriver.common.by import By
from pagesinventory_page import InventoryPage


class LoginPage:
    """
    Page Object для страницы авторизации интернет-магазина.
    """

    def __init__(self, driver):
        """
        Инициализация страницы логина.

        :param driver: WebDriver (экземпляр браузера)
        """
        self.driver = driver

    def open(self) -> "LoginPage":
        """
        Открывает страницу авторизации в браузере.

        :return: Экземпляр LoginPage для цепочки вызовов
        """
        self.driver.get("https://www.saucedemo.com/")
        return self

    def login(self, username: str, password: str) -> InventoryPage:
        """
        Выполняет вход в систему.

        :param username: Имя пользователя
        :param password: Пароль
        :return: Экземпляр страницы InventoryPage (список товаров)
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name"
        ).send_keys(username)
        self.driver.find_element(
            By.CSS_SELECTOR, "#password"
        ).send_keys(password)
        self.driver.find_element(
            By.CSS_SELECTOR, "#login-button"
        ).click()
        return InventoryPage(self.driver)
