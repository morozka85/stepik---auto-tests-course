from selenium import webdriver
import time 

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
    input3.send_keys("Smolensk@mail.mu")
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('[type="submit"]')
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
    
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    print(welcome_text)
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла
	