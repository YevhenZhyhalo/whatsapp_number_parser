from selenium import webdriver
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
import os
import time
import csv
import re

fn = ['Name', 'Given Name', 'Phone 1 - Type', 'Phone 1 - Value']


chromedriver = os.path.join(os.path.expanduser('~'),
                            'Downloads', 'chromedriver')
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://web.whatsapp.com")
wait = ui.WebDriverWait(driver, 20)

input("Enter any keyword after scanning QR code.\n ")


left_panel = driver.find_elements_by_class_name("_210SC")

contacts = 1


with open('conts.csv', mode='w') as csv_file:
	writer = csv.DictWriter(csv_file, fieldnames=fn)
	writer.writeheader()
	k = 0
	for panel in left_panel:
		panel.click()
		name = driver.find_element_by_xpath(
            "//*[@id='main']/header/div[2]/div[1]/div/span").get_attribute('title')
		panel_parsed = driver.find_element_by_xpath(
		"//*[@id='main']/header/div[2]/div[2]/span")

		contacts = panel_parsed.get_attribute('title')

		if(contacts == 'данные группы'):  
			time.sleep(2)# wait until group info load
			panel_parsed = driver.find_element_by_xpath(
                "//*[@id='main']/header/div[2]/div[2]/span")
			contacts = panel_parsed.get_attribute('title').split(',')

			i = 1
			for number in contacts:
				if('+' in number):
					writer.writerow({fn[0]: name + str(i), fn[1]: name +str(i), fn[2]: 'Mobile', fn[3]: number})
				i+=1
				if(i==2):
					print(name+" is parsing now")

		else:  # ?????? nuzhno li???
			panel_parsed.click()
			time.sleep(1)
			paneltwo = driver.find_element_by_xpath(
                "//*[@id='app']/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[4]/div[3]/div/div/span/span")
			number = paneltwo.text
			writer.writerow({fn[0]: name, fn[1]: name , fn[2]: 'Mobile', fn[3]: number})


















    #text_file.write(contacts + '\n')
# text_file.close()


#Find_box= driver.find_elements_by_class_name("_3FRCZ")
#Find_box.send_keys("+380 73 141 6003")

#user = driver.find_element_by_xpath("//span[@title='{}']".format("Sasha"))
# user.click()

#text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
# text_box.send_keys("Hiiii")
# contacts = find_element_by_xpath("//*[@id="main"]/header/div[2]/div[2]/span")
#button = driver.find_element_by_class_name("_1U1xa")
# button.click()
