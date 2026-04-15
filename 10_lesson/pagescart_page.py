from selenium.webdriver.common.by import By
from pagescheckout_page import CheckoutPage


class CartPage:
    """
    Page Object для страницы корзины интернет-магазина.
    """

    def __init__(self, driver):
        """
        Инициализация страницы корзины.

        :param driver: WebDriver (экземпляр браузера)
        """
        self.driver = driver

    def checkout(self) -> CheckoutPage:
        """
        Нажимает кнопку оформления заказа и переходит на страницу оформления.

        :return: Экземпляр страницы CheckoutPage
        """
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        return CheckoutPage(self.driver)
