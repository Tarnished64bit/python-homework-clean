from selenium import webdriver
from pageslogin_page import LoginPage


def test_shop_purchase():
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)

    inventory_page = login_page.open().login("standard_user", "secret_sauce")

    inventory_page.add_to_cart("add-to-cart-sauce-labs-backpack")
    inventory_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    inventory_page.add_to_cart("add-to-cart-sauce-labs-onesie")

    cart_page = inventory_page.go_to_cart()
    checkout_page = cart_page.checkout()

    checkout_page.fill_form("Иван", "Петров", "123456")

    total = checkout_page.get_total()
    assert total == 58.29

    driver.quit()
