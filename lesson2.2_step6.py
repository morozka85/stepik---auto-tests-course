from selenium import webdriver
import time 
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://SunInJuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)
    
	# находим х
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	print(x)
	# считаем и вставляем ответ в поле
	y = calc(x)
	print(y)
	#scroll
	browser.execute_script("window.scrollBy(0, 150);")	
	
	input1 = browser.find_element_by_id("answer")
	input1.send_keys(y)
    
	# Выбираем кнопки
	button1 = browser.find_element_by_id("robotCheckbox")
	button1.click()
	button2 = browser.find_element_by_id("robotsRule")
	button2.click()
	
	# Отправляем заполненную форму
	submit = browser.find_element_by_class_name("btn.btn-primary")
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