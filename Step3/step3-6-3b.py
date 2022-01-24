import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

s = ''
urls = ['https://stepik.org/lesson/236895/step/1',
     'https://stepik.org/lesson/236896/step/1',
     'https://stepik.org/lesson/236897/step/1',
     'https://stepik.org/lesson/236898/step/1',
     'https://stepik.org/lesson/236899/step/1',
     'https://stepik.org/lesson/236903/step/1',
     'https://stepik.org/lesson/236904/step/1',
     'https://stepik.org/lesson/236905/step/1']
count = 0

def compute():
    answer = math.log(int(time.time()))
    print(answer)
    return answer


@pytest.fixture
def browser(scope='function'):
    browser = webdriver.Firefox()
    yield browser
    browser.quit()


@pytest.mark.parametrize('links', urls)
def test_compute(browser, links):
    link = links
    browser.implicitly_wait(10)
    browser.get(link)
    time.sleep(5)
    answer = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.textarea')))
    answer.send_keys(str(compute()))
    but = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission')))
    but.click()
    feed = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          '.smart-hints__hint'))).text
    print(feed)
    


        
    
        
        
    




