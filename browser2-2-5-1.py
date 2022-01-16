import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

url = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Firefox()
    browser.get(url)

    but = browser.find_element(By.XPATH, '//button')
    browser.execute_script('return arguments[0].scrollIntoView(true)', but)
    but.click()
    assert True
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
