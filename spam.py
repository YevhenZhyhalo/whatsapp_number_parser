from selenium import webdriver
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
import os,time,csv,re,datetime
import urllib.request as url


#variables


#init app
chromedriver = os.path.join(os.path.expanduser('~'),
                            'Downloads', 'chromedriver')
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://web.whatsapp.com")
wait = ui.WebDriverWait(driver, 20)
input("Press enter after scanning QR.\n ")
numbers= open("numbers.txt",'r').read().split('\n')
Find_box= driver.find_elements_by_class_name("_3FRCZ")
text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')## may not be right
button = driver.find_element_by_class_name("_1U1xa")


for num in numbers:
	find_box.clear()
	find_box.click()
	find_box.send_keys(num)
	find_box.send_keys('\n')
	text_box.send_keys("")
	text_box.send_keys('\n')
	#button.click()