import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"
names = ['Алексей', 'Елисеев', 'Kamchatka', 'Russia']

try:
    browser = webdriver.Firefox()
    browser.get(link)
    input1 = browser.find_element(By.XPATH, '//input[@name="first_name"]')
    input1.send_keys(names[0])
    input2 = browser.find_element(By.XPATH, '//input[@name="last_name"]')
    input2.send_keys(names[1])
    input3 = browser.find_element(By.XPATH, '//input[@name="firstname"]')
    input3.send_keys(names[2])
    input4 = browser.find_element(By.XPATH, '//input[@id="country"]')
    input4.send_keys(names[3])
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
