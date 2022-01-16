import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

url = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Firefox()
    browser.get(url)

    but = browser.find_element(By.XPATH, '//button')
    _ = but.location_once_scrolled_into_view
    but.click()
    assert True
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
