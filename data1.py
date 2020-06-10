import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time, os
#import schedule as sc
print("Working")
from flask_pymongo import PyMongo
from flask import Flask


from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-default-apps")
chrome_options.add_argument("--disable-media-source")
chrome_options.add_argument("--mute-audio")
GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
chrome_bin = os.environ.get('GOOGLE_CHROME_SHIM', None)
chrome_options.binary_location = chrome_bin




app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb+srv://devtotti:jankulovski@newclustera-c85ej.mongodb.net/pizzas?retryWrites=true&w=majority"
app.config["MONGO_URI"] = "mongodb+srv://michael:Lagos12#@cluster0-lnbg3.mongodb.net/pizzas?retryWrites=true&w=majority"
mongo = PyMongo(app)

#from marco import *
from cici import *
from offers import *




def chrome_drive(firm, website, link):
	#driver = webdriver.Chrome(executable_path = '/home/devtotti/Workspace/extensions/chromedriver_linux64/chromedriver', options=chrome_options)#for local test remove comments
	driver = webdriver.Chrome(executable_path = CHROMEDRIVER_PATH ,options=chrome_options)#for deployment, remove comments

	driver.wait = WebDriverWait(driver, 5)

	firm = str(firm)
	company = str(website)
	url = str(link)
	
	driver.get(url)
	time.sleep(5)
	deals = driver.find_elements_by_class_name("item.showDeals.code ")
	for data in deals:
		but1 = data.find_element_by_class_name("title.cpbtn").text
		but2 = data.find_element_by_class_name("desc").text
		but3 = data.find_element_by_class_name("buttonRight")
		but4 = but3.find_element_by_tag_name("a")
		but5 = but4.get_attribute("data-clipboard-text")
		disc_type = data.find_element_by_class_name("badge.coupon").text


		print(but1, but2, but5, disc_type)

		response = saveToCloud(firm, company, but1, but2, but5, disc_type)

		print(response)
		
	

	discount = driver.find_elements_by_class_name("item.showDeals.discount  ")
	for data in discount:
		but1 = data.find_element_by_class_name("title.cpbtn").text
		but2 = data.find_element_by_class_name("desc").text
		disctype = data.find_element_by_class_name("badge.discount").text
		but5 = "Get offer on website"

		print(but1, but2, but5, disctype)

		response = saveToCloud(firm, company, but1, but2, but5, disctype)

		print(response)

	return driver



def saveToCloud(firm, ada, bada, cada, dada, fada):
	db = mongo.db.coupons

	firm = str(firm)
	website = str(ada)
	discount = str(bada)
	summary = str(cada)
	code = str(dada)
	discountType = str(fada)

	count = []

	for field in db.find():

		if str(field['company']) == firm and str(field['websiteName']) == website and str(field['pizzaSummary']) == summary and str(field['discount']) == discount and str(field['couponCode']) == code and str(field['discountType']) == discountType:
			count.append(1)

		else:
			pass




	if len(count) > 0:
		print("Data exists in the database")
		response = "Success"


	else:
		data = {"company":firm, "websiteName":website, "pizzaSummary": summary, "discount":discount, "couponCode":code, "discountType":discountType}

		try:
			save = db.insert_one(data)

			print("Data saved Successfully!")

			response = "Success!"

		except Exception as error:
			print("Error saving into database: "+str(error))
			response = "Failed!"


	return response


def major():
	marcos()




def marcos():
	print("marcosPizza")
	firm = "marcosPizza"
	website = "https://www.marcos.com/"
	url = "https://slickdeals.net/coupons/marcos-pizza/"
	driver = chrome_drive(firm, website, url)
	papaMurphys(driver)



def papaMurphys(driver):
	print("papaMurphy's")
	website = "https://www.papamurphys.com/"
	url = "https://slickdeals.net/coupons/papa-murphys/"
	firm = "papaMurphys"
	chrome_drive(firm, website, url)
	jetsPizza(driver)




def jetsPizza(driver):
	print("jetsPizza")
	website = "https://www.jetspizza.com"
	url = "https://slickdeals.net/coupons/jets-pizza/"
	firm = "jetsPizza"
	chrome_drive(firm, website, url)
	blazePizza()


def blazePizza(driver):
	print("blazePizza")
	website = "https://www.blazepizza.com"
	url = "https://slickdeals.net/coupons/blaze-pizza/"
	firm = "blazePizza"
	chrome_drive(firm, website, url)
	print("Closing chrome tabs")
	roundTable()



def roundTable(driver):
	print("roundTablePizza")
	website = "https://www.roundtablepizza.com"
	url = "https://slickdeals.net/coupons/round-table-pizza/"
	firm = "roundTable"
	chrome_drive(firm, website, url)
	print("Closing chrome tabs")
	driver.close()
	cicis()








def cicis():
	response = ciciPizza()
	caliKitchen()
	


def caliKitchen():
	print("california-pizza-kitchen")
	url = "https://www.offers.com/california-pizza-kitchen/"
	firm = "cpkPizza"
	website = "https://www.cpk.com/"
	response = crawl_exctract(url, firm, website)
	sBarro()



def sBarro():
	print("sBarro pizza")
	url = "https://www.offers.com/sbarro/"
	firm = "sbarro"
	website = "https://sbarro.com/"
	response = crawl_exctract(url, firm, website)






