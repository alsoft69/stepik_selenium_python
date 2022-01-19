from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/math.html"

def calc(value):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Firefox() #запуск в Firefox
    browser.get(link)
    
    val = webrovser.find_by_element(By.ID, 'input_value')
    val_text = val.text
    print(val_text)
    x = calc(val_text)
    browser.find_by_element(By.ID, 'answer').
    browser.find_by_element(By.ID, 'robotCheckBox').click()
    browser.find_by_element(By.ID, 'robotsRule').click
    
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
