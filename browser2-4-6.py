from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.implicitly_wait(5)
# установка времени ожидания 5 сек для поиска элементов
browser.get("http://suninjuly.github.io/cats.html")

time.sleep(1)
button = browser.find_element_by_id("button")

time.sleep(10)
browser.quit()
