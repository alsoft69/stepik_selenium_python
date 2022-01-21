import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def compute():
    answer = math.log(int(time.time()))
    print(answer)
    return answer


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()


class Test_UFO():
    s = ''
    urls = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1']

    @pytest.mark.parametrize('links', urls)
    def test_compute(self, browser, links):
        link = links
        browser.implicitly_wait(10)
        browser.get(link)

        text = browser.find_element_by_class_name('textarea')
        print('Found textarea')
        text.send_keys(str(compute()))
        button = browser.WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(By.CLASS_NAME, 'submit-submission'))
        button.click()
        txt = browser.WebDriverWait(browser, 5).until(
            EC.visibiliti_of_element_located(By.CLASS_NAME, 'textarea').text)
        if txt != 'Correct!':
            self.s += txt
        assert txt == False
        print(s)
        
    
        
        
    




