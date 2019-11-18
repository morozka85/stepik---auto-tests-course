from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

def sum(x,y):
	return str(int(x)+int(y))

try:
	link = "http://suninjuly.github.io/selects2.html"
	browser = webdriver.Chrome()
	browser.get(link)
    
	# находим х
	x_element = browser.find_element_by_id("num1")
	x = x_element.text    
	print(x)
	# находим y
	y_element = browser.find_element_by_id("num2")
	y = y_element.text    
	print(y)
	# считаем
	sum = sum(x,y)
	print(sum)
	    
	# Выбираем значение
	select = Select(browser.find_element_by_id("dropdown"))
	select.select_by_value(sum) # ищем элемент с суммой
	
	# Отправляем заполненную форму
	submit = browser.find_element_by_class_name("btn.btn-default")
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