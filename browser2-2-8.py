import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

url = "http://suninjuly.github.io/file_input.html"
myfile = 'test.txt'

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 

    browser = webdriver.Firefox()
    browser.get(url)
    fname = browser.find_element(By.NAME, 'firstname')
    fname.send_keys('firstname')
    lname = browser.find_element(By.NAME, 'lastname')
    lname.send_keys('lastname')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('email@email.com')
    sender = browser.find_element(By.ID, 'file')
    sender.send_keys(file_path)
    but = browser.find_element(By.XPATH, '//button')
    but.click()
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
