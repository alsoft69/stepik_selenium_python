from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.implicitly_wait(5)
# установка времени ожидания 5 сек для поиска элементов
browser.get("http://suninjuly.github.io/wait2.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
