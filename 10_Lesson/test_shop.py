import allure
from selenium import webdriver
from pageslogin_page import LoginPage


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Проверка оформления заказа")
@allure.description("Авторизация, добавление трёх товаров в корзину, оформление заказа, проверка итоговой суммы")
def test_shop_purchase():
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)

    with allure.step("Открыть страницу логина и авторизоваться"):
        inventory_page = login_page.open().login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        inventory_page.add_to_cart("add-to-cart-sauce-labs-backpack")
        inventory_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
        inventory_page.add_to_cart("add-to-cart-sauce-labs-onesie")

    with allure.step("Перейти в корзину и оформить заказ"):
        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.checkout()

    with allure.step("Заполнить форму оформления заказа"):
        checkout_page.fill_form("Иван", "Петров", "123456")

    with allure.step("Получить итоговую сумму и проверить её"):
        total = checkout_page.get_total()
        assert total == 58.29

    driver.quit()
