import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
    """Вычисление выражение"""
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд,
    # пока кнопка не станет кликабельной
    best_price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    button = browser.find_element(By.ID, 'book')
    button.click()

    num = browser.find_element(By.ID, 'input_value').text
    print('Получено число: ',end='')
    print(num)
    res = calc(num)
    print('Получен результат вычисления: ', end='')
    print(res)
    inp = browser.find_element(By.ID, 'answer')
    inp.send_keys(res)
    print('Результат отправлен!')

    but = browser.find_element(By.ID, 'solve')
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
    browser.quit()
