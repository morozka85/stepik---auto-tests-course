from selenium import webdriver
import time 
import os
with open("test.txt", "w") as file:
	content = file.write("automationbypython")  # create test.txt file

try:
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)
    
	#заполняем поля
	firstname = browser.find_element_by_name("firstname")
	firstname.send_keys("firstname")
	lastname = browser.find_element_by_name("lastname")
	lastname.send_keys("lastname")
	email = browser.find_element_by_name("email")
	email.send_keys("email")
	
	#выбираем файл
	file1 = browser.find_element_by_id("file")
	# получаем путь к директории текущего исполняемого файла 
	current_dir = os.path.abspath(os.path.dirname(__file__))
	# добавляем к этому пути имя файла     
	file_path = os.path.join(current_dir, 'file.txt')           
	file1.send_keys(file_path)
	
	
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