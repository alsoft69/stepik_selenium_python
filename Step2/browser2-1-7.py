import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Firefox() #запуск в Firefox
    browser.get(link)

    treasure = browser.find_element(By.ID, 'treasure')
    tr_val = treasure.get_attribute('valuex')
    print('Число - ', tr_val)
    znach = calc(tr_val)
    print('Значение - ', znach)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(znach)
    
    chk = browser.find_element(By.ID, 'robotCheckbox')
    chk.click()

#    pr = browser.find_element(By.ID, 'peopleRule')

    rr = browser.find_element(By.ID, 'robotsRule')
    rr.click()

    sub = browser.find_element(By.CLASS_NAME, 'btn')
    sub.click()
    
finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
