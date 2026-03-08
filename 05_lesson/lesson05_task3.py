from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

    input_field.send_keys("12345")
    print("Введено 12345")
    time.sleep(1)

    input_field.clear()
    print("Поле очищено")
    time.sleep(1)

    input_field.send_keys("54321")
    print("Введено 54321")
    time.sleep(2)

finally:
    driver.quit()
