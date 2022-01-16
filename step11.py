import time
from selenium import webdriver

def step9():
    try: 
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Firefox()
        browser.get(link)
        #Признак обязательного для заполнения поля - атрибут required
        input1 = browser.find_elements_by_xpath("//input[@required]")
        #Для того, чтобы заранее определить, следует коду упасть или нет,
        #лучше привязываться не к конкретным эл-там на странице,
        #а к их количеству
        countElemReq = 3
        if len(input1) != countElemReq:
            print('На странице не обнаружено необходимого количества элементов')
            browser.quit()
            exit()
        else: 
            for elem in input1:
                elem.send_keys('Привет!')
            # Ваш код, который заполняет обязательные поля
        

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

step9()
