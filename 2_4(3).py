from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def calc(num2):
	return str(math.log(abs(12*math.sin(int(num2)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	but = WebDriverWait(browser, 12).until(
			EC.text_to_be_present_in_element((By.ID, "price"), "$100")
		)
	
	but_cl = browser.find_element_by_id("book").click()

	num = browser.find_element_by_id("input_value")
	num2 = calc(int(num.text))
	
	inputnum = browser.find_element_by_id("answer")
	inputnum.send_keys(num2)

	button = browser.find_element_by_id("solve")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	but_cl = browser.find_element_by_id("solve").click()
	
finally:
	time.sleep(5)
	browser.quit()

