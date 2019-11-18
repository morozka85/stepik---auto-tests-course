from selenium import webdriver
import time 

try:
	link = "https://SunInJuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
    #search button and click
	button = browser.find_element_by_tag_name("button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()
	assert True
 
except Exception as error:
    print(f'{error}')
   
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла