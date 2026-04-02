
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_purchase():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(
        By.CSS_SELECTOR, "#user-name"
        ).send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        )
    ).click()

    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
    ).click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"
    ).click()

    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    total_element = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".summary_total_label")
            )
    )
    total_text = total_element.text
    total_value = float(total_text.replace("Total: $", ""))
    assert total_value == 58.29

    driver.quit()
