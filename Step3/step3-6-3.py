import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1']

s = ''

def compute():
    answer = math.log(int(time.time()))
    return answer

@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()

def test_compute(browser):
    for link in links:
        browser.get(link)
        time.sleep(10)
        answer = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'ember_view')))
        ans = browser.find_element(By.CLASS_NAME, 'ember_view')
        if ans: print('Found ans')
        ans.send_keys(compute())
        txt = browser.find_element(By.ID, 'code-run_notify').get()
        print(txt)
        
        
    




