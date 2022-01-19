import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Firefox() #запуск в Firefox
    browser.get(link)
    inp = browser.find_element(By.CSS_SELECTOR,
                               '.first_block .first_class .first')
    inp.send_keys('Alex')
    inp = browser.find_element(By.CSS_SELECTOR,
                               '.first_block .second_class .second')
    inp.send_keys('Alex')
    inp = browser.find_element(By.CSS_SELECTOR,
                               '.first_block .third_class .third')
    inp.send_keys('Alex@alex.ru')
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    time.sleep(5)
    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
