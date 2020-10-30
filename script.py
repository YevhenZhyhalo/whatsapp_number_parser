from selenium import webdriver
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
import os,time,csv,re,datetime
import urllib.request as url
import vcfpy as vcf

#variables
fn = ['Name', 'Given Name', 'Phone 1 - Type', 'Phone 1 - Value']
file_path  ='contacts-' +datetime.datetime.now(tz=None).strftime("%h-%d_%H:%M")+'.csv'

#init app
chromedriver = os.path.join(os.path.expanduser('~'),
                            'Downloads', 'chromedriver')
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://web.whatsapp.com")
wait = ui.WebDriverWait(driver, 20)
input("Press enter after scanning QR.\n ")




#PEZDEC
left_panel = driver.find_elements_by_class_name("_210SC")
with open(file_path, mode='w+') as csv_file:
	writer = csv.DictWriter(csv_file, fieldnames=fn)
	writer.writeheader()
	
	for panel in left_panel:
		panel.click()
		name = driver.find_element_by_xpath(
            "//*[@id='main']/header/div[2]/div[1]/div/span").get_attribute('title')
		panel_parsed = driver.find_element_by_xpath(
		"//*[@id='main']/header/div[2]/div[2]/span")

		contacts = panel_parsed.get_attribute('title')

		if(contacts == 'данные группы'):  
			print(name+" is parsing now")
			group_path = 'Groups/'+name
			try:
				os.makedirs(group_path)
			except Exception:
				group_path = group_path+'_repeat'
				name = name +'_repeat'
				os.makedirs(group_path)


			try:#group pp parse
				link = driver.find_element_by_xpath("//*[@id='main']/header/div[1]/div/img").get_attribute('src')
				driver.execute_script(f'window.open();')				
				driver.switch_to.window(driver.window_handles[-1])
				driver.get(link)
				picture = driver.find_element_by_xpath('/html/body/img')
				image = picture.screenshot(group_path+'/pp.png')
				driver.close()
				driver.switch_to.window(driver.window_handles[0])
			except Exception:
				print("no photo")


			time.sleep(2)# Write logic
			panel_parsed = driver.find_element_by_xpath(
                "//*[@id='main']/header/div[2]/div[2]/span")
			contacts = panel_parsed.get_attribute('title').split(',')

			i = 1
			with open(group_path+'/contacts.csv', mode='w+') as csv_group_file:
				group_writer = csv.DictWriter(csv_group_file, fieldnames=['name','number'])
				group_writer.writeheader()


				for number in contacts:#bolshaya dira
					group_writer.writerow({'name':name+str(i),'number':number})
					if('+' in number):
						writer.writerow({fn[0]: name + str(i), fn[1]: name +str(i), fn[2]: 'Mobile', fn[3]: number})
					i+=1
					


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
