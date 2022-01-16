from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WBW
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

url = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Firefox()
    browser.get(url)
#    wait = WBW(browser, 20).until(EC.visibility_of_all_elements_located(By.TYPE_NAME, 'text'))
    sleep(10)
    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys('Jndtn')
    print('Найдено элементов:', len(elements))

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    sleep(30)
    browser.quit()

