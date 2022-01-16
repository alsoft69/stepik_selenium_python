import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

url = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def scr(name):
    browser.execute_script('return arguments[0].scrollIntoView(true)', name)

try:
    browser = webdriver.Firefox()
    browser.get(url)
    browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser.current_window_handle)
    confirm = browser.switch_to.alert
    time.sleep(1)
    confirm.accept()
    time.sleep(1)
    new_wind = browser.window_handles[0]
    print(browser.current_window_handle)
    browser.switch_to.window(new_wind)
##    url2 = 'http://suninjuly.github.io/alert_redirect.html'
##    browser.get(url2)
    num = browser.find_element(By.ID, 'input_value').text
    print('Получено число: ',end='')
    print(num)
    res = calc(num)
    print('Получен результат вычисления: ', end='')
    print(res)
    inp = browser.find_element(By.ID, 'answer')
    scr(inp)
    inp.send_keys(res)
    print('Результат отправлен!')
##    chk = browser.find_element(By.ID, 'robotCheckbox')
##    chk.click()
##    print('отмечен чекбокс')
###    pr = browser.find_element(By.ID, 'peopleRule')
##
##    rr = browser.find_element(By.ID, 'robotsRule')
##    rr.click()
##    print('Отмечена радиокнопка')
    but = browser.find_element(By.XPATH, '//button')
    scr(but)
    but.click()
    assert True
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
