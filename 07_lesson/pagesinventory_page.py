from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, item_id):
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"#{item_id}"))
        ).click()
        return self

    def go_to_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link"
        ).click()
        from pagescart_page import CartPage
        return CartPage(self.driver)
