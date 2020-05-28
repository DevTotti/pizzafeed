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
app.config["MONGO_URI"] = "mongodb+srv://devtotti:jankulovski@newclustera-c85ej.mongodb.net/pizzas?retryWrites=true&w=majority"
mongo = PyMongo(app)





def chrome_drive():
	#driver = webdriver.Chrome(executable_path = '/home/devtotti/Workspace/extensions/chromedriver_linux64/chromedriver', options=chrome_options)#for local test remove comments
	driver = webdriver.Chrome(executable_path = CHROMEDRIVER_PATH ,options=chrome_options)#for deployment, remove comments

	driver.wait = WebDriverWait(driver, 5)


	return driver


def get_data(driver):

	pizzaCompanies = [
	["https://sbarro.com/","https://www.offers.com/sbarro/","sbarro"],
	["https://www.cpk.com/","https://www.offers.com/california-pizza-kitchen/","cpkPizza"]
	]	

	for pizzaCompany in pizzaCompanies:
		firm = str(pizzaCompany[2])
		company = str(pizzaCompany[0])
		url = str(pizzaCompany[1])


		driver.get(url)
	
		stats = driver.find_element_by_id("merchant-stats")
		count = stats.find_element_by_class_name("value").text
	
		blocks = driver.find_elements_by_class_name("offerstrip")
		total = int(count)

		for block in blocks[0:total]:
			block = block.text
			block = block.split("\n")
		
			if 'CODE:' in block:
				couponCode = block[6]
				disc_type = "COUPON"
				disc = block[0]
				summary = block[3]

			elif block[0] == 'SALE':
				couponCode = "Get Offers on website and stores"
				disc_type = "SALES & OFFERS"
				summary = block[1]
				disc = block[3]



			print(couponCode, disc, disc_type, summary)
			response = saveToCloud(firm,company,disc,summary,couponCode,disc_type)


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
	driver = chrome_drive()
	driver = get_data(driver)
	driver.close()




		



