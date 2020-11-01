from selenium import webdriver
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
import os,time,csv,re,datetime
import urllib.request as url


#variables

path = '/home/gekailovegeka/whatsapp_number_parser/Groups'
#init app
chromedriver = os.path.join(os.path.expanduser('~'),
                            'Downloads', 'chromedriver')
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://web.whatsapp.com")
wait = ui.WebDriverWait(driver, 20)
input("Press enter after scanning QR.\n ")

i = 0
for dir in os.walk('/home/gekailovegeka/whatsapp_number_parser/Groups/'):     
	if(i!=0):
		print(dir[0])
		button = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div/span')
		button.click()
		new_group = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div[1]/div[2]/div/div')
		new_group.click()
		numbers= open(dir[0]+'/contacts.csv','r').read().split('\n')
		find_box= driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input')
		for num in numbers:
			find_box.clear()
			find_box.click()
			find_box.send_keys(num)
			find_box.send_keys('\n')
		finish_box = find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div/div[2]')
		finish_box.click()
		finish_box.send_keys(dir[0].split('/')[-1])
		finish_box.send_keys('\n')
		with open('group_names.txt','a+') as group_files:
				group_files.write(dir[0].split('/')[-1]+'\n')

	i = 1+i











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
