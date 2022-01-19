import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
text_ok = "Congratulations! You have successfully registered!"

class TestReg(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Firefox() #запуск в Firefox
        browser.get(link1)
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

        self.assertEqual(text_ok, welcome_text, "Element 'Last name' not found")
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_reg2(self):
        browser = webdriver.Firefox() #запуск в Firefox
        browser.get(link2)
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

        self.assertEqual(text_ok, welcome_text, "Element 'Last name' not found")
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == '__main__':
    unittest.main()
                         
