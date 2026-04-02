from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")

    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")

    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    )
    login_button.click()
    time.sleep(1)

    success_message = driver.find_element(
        By.CSS_SELECTOR,
        ".flash.success"
    )
    print("Сообщение:", success_message.text)

    time.sleep(2)

finally:
    driver.quit()
