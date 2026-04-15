from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pagescart_page import CartPage


class InventoryPage:
    """
    Page Object для страницы списка товаров интернет-магазина.
    """

    def __init__(self, driver):
        """
        Инициализация страницы товаров.

        :param driver: WebDriver (экземпляр браузера)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, item_id: str) -> "InventoryPage":
        """
        Добавляет товар в корзину по ID кнопки.

        :param item_id: HTML id элемента кнопки добавления товара
        :return: Экземпляр InventoryPage для цепочки вызовов
        """
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"#{item_id}"))
        ).click()
        return self

    def go_to_cart(self) -> CartPage:
        """
        Переходит в корзину.

        :return: Экземпляр страницы CartPage
        """
        self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link"
        ).click()
        return CartPage(self.driver)
