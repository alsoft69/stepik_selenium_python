import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

url = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    """Вычисление выражение"""
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Firefox()       # запуск драйвера браузера
    browser.get(url)                    # переход на страницу url
    print(browser.current_url)

    browser.find_element(By.CLASS_NAME, 'trollface').click()
    # поиск элемента на странице по имени класса
    time.sleep(2)
    print(browser.window_handles)
    # получение списка открытых страниц
    browser.switch_to.window(browser.window_handles[1])
    # переход на вторую страницу
    time.sleep(2)
    print(browser.current_url)
    time.sleep(3)

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

    but = browser.find_element(By.XPATH, '//button')
    but.click()

    alert = browser.switch_to.alert
    # получение сообщения
    time.sleep(1)
    print(alert.text)
    # получение текста из окна сообщения
    num_answer = alert.text.split(': ')[-1]
    # получение числа из текста сообщения
    alert.accept()
    # нажатие кнопки в окне сообщения
    print(num_answer)
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
