from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
	
try:
	# говорим WebDriver искать каждый элемент в течение 5 секунд
	browser.implicitly_wait(5)
	button = browser.find_element_by_id("verify")
	button.click()
	message = browser.find_element_by_id("verify_message")

	assert "successful" in message.text
	mtext = message.text
	print(mtext)
	
except Exception as error:
    print(f'{error}')
    #print(welcome_text)

finally:
    # успеваем скопировать код за 30 секунд
    #time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла