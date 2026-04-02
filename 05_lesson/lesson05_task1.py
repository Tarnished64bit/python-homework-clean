from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/classattr")

    blue_button = driver.find_element(
        By.CSS_SELECTOR,
        "button.btn-primary"
    )

    blue_button.click()
    print("Кнопка нажата.")
    time.sleep(2)

finally:
    driver.quit()
