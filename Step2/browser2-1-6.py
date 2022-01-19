import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Firefox() #запуск в Firefox
    browser.get(link)
    
    chk = browser.find_element(By.ID, 'robotCheckbox')
    chk_chk = chk.get_attribute('required')
    print('"I`m robot" checkbox is', chk_chk)
    assert chk_chk is not None, 'CheckBox is not selected by default'
    pr = browser.find_element(By.ID, 'peopleRule')
    pr_chk = pr.get_attribute('checked')
    print('"People rule" radiobutton checked is', pr_chk)
    assert pr_chk is not None, 'People_rule radiobutton is not selected'
    rr = browser.find_element(By.ID, 'robotsRule')
    rr_chk = rr.get_attribute('checked')
    print('"Robot rule" radiobutton checked is', rr_chk)
    assert rr_chk is None, 'Robot_rule radiobutton is selected'
    sub = browser.find_element(By.CLASS_NAME, 'btn')
    sub_en = sub.get_attribute('disabled')
    print('Button "Submit" status=disabled is', sub_en)
    assert sub_en is None
    time.sleep(10)
    print('time for 10 sec')
    sub = browser.find_element(By.CLASS_NAME, 'btn')
    sub_en = sub.get_attribute('disabled')
    print('Button "Submit" status=disable is', sub_en)
    assert sub_en is None
    
finally:

    # закрываем браузер после всех манипуляций
    browser.quit()
