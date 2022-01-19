import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/math.html"

def calc(value):
    return str(math.log(abs(12*math.sin(int(value)))))

try:
    browser = webdriver.Firefox() #запуск в Firefox
    browser.get(link)
    
    val = browser.find_element(By.ID, 'input_value')
    val_text = val.text
    print(val_text)
    x = calc(val_text)
    browser.find_element(By.ID, 'answer').send_keys(x)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CLASS_NAME, 'btn').click()
    
finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
