from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	browser.implicitly_wait(5)
    
	# Click button "BOOK" when price 100
	price = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
	book = browser.find_element_by_id("book")
	book.click()

	# находим х
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	print(x)
	# считаем и вставляем ответ в поле
	y = calc(x)
	print(y)
	input1 = browser.find_element_by_id("answer")
	input1.send_keys(y)
    	
	# Отправляем заполненную форму
	submit = browser.find_element_by_id("solve")
	submit.click()
 
except Exception as error:
    print(f'{error}')
    #print(welcome_text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла