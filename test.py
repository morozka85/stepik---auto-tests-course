from selenium import webdriver
import time 

link = "https://anketa-test.alfa-bank.kz/login"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_class_name("input__control")
    input1.send_keys("+7 (702) 159-42-34")
    button = browser.find_element_by_class_name("button__text")
    button.click()
    time.sleep(30)
    input2 = browser.find_element_by_css_selector('input[maxlength="4"]')
    input2.send_keys("1234")
    
    
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
	
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла
	