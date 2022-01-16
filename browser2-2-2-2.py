import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

url = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Firefox()
    browser.get(url)

    num_1 = int(browser.find_element(By.XPATH, '//span[@id="num1"]').text)
    num_2 = int(browser.find_element(By.XPATH, '//span[@id="num2"]').text)
    summa = str(num_1+num_2)
    sel = browser.find_element(By.XPATH, f'//select/option[@value={summa}]')
    sel.click()
    but = browser.find_element(By.XPATH, '//button')
    but.click()
finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
