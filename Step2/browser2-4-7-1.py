from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Firefox()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд,
# пока кнопка не станет кликабельной
best_price = WebDriverWait(browser, 5).until(
        EC.element_to_be_present_in_element((By.ID, "price"), '$100'))
button = browser.find_element(By.ID, 'book')
button.click()

