from selenium import webdriver
import time 
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)
    # Click button "I want to go on a magical journey!"
	button1 = browser.find_element_by_class_name("trollface.btn")
	button1.click()
	#Vsplyvayusee okno, click OK
	#confirm = browser.switch_to.alert
	#confirm.accept()
	#time.sleep(1)

	#Another window
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)

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