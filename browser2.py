import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"
names = ['Алексей', 'Елисеев', 'Kamchatka', 'Russia']

try:
    browser = webdriver.Firefox()
    browser.get(link)
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys(names[0])
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys(names[1])
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys(names[2])
    input4 = browser.find_element_by_id("country")
    input4.send_keys(names[3])
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
