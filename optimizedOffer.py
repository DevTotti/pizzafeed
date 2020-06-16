import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time, os
#import schedule as sc
print("Working offer")
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
app.config["MONGO_URI"] = "mongodb+srv://michael:Lagos12#@cluster0-3gczm.mongodb.net/pizzas?retryWrites=true&w=majority"
mongo = PyMongo(app)





def chrome_drive():
	#driver = webdriver.Chrome(executable_path = '/home/devtotti/Workspace/extensions/chromedriver_linux64/chromedriver', options=chrome_options)#for local test remove comments
	driver = webdriver.Chrome(executable_path = CHROMEDRIVER_PATH ,options=chrome_options)#for deployment, remove comments

	driver.wait = WebDriverWait(driver, 5)


	return driver


def get_data(driver):

	blocks = []
	


	pizzaCompanies = [
	["https://sbarro.com/","https://www.offers.com/sbarro/","sbarro"],
	["https://www.cpk.com/","https://www.offers.com/california-pizza-kitchen/","cpkPizza"],
	["https://www.hungryhowies.com","https://www.offers.com/hungry-howies/","hungryHowie"],
	["https://www.unos.com","https://www.offers.com/uno-pizzeria-and-grill/","unoChicago"],
	["https://www.papaginos.com","https://www.offers.com/papa-ginos/","papaGinos"],
	["https://www.godfathers.com","https://www.offers.com/godfathers-pizza/","godFathers"]
	]	

	for pizzaCompany in pizzaCompanies:
		


		blocks[:] = []
		
		
		firm = str(pizzaCompany[2])
		company = str(pizzaCompany[0])
		url = str(pizzaCompany[1])
		print(firm)


		driver.get(url)
	
		stats = driver.find_element_by_id("merchant-stats")
		count = stats.find_element_by_class_name("value").text
	
		blucks = driver.find_elements_by_class_name("offerstrip")
		total = int(count)

		blocks = [i for i in blucks]
		origin = True


		while origin:
			length = len(blocks)
			print(len(blocks))
			for index, bluck in enumerate(blocks):
				#print(bluck)
				#indice =  int(blocks.index(bluck))
				#print(indice)

				block = bluck.text
				#print(block)
				#block = block.split("\n")

				if 'SALE' in block and not 'Reveal Code' in block and not 'Expired' in block:
					blocks.remove(bluck)
					##del(blocks[indice])

					block = block.split("\n")
					print(block)
					couponCode = "Get Offers on website and stores"
					disc_type = "SALES & OFFERS"
					summary = block[1]
					disc = block[3]

					print(couponCode, disc, disc_type, summary)
					response = saveToCloud(firm, company, disc, summary, couponCode, disc_type)
					print(response)

				elif 'Expired' in block:
					blocks.remove(bluck)

				elif 'Reveal Code' not in block:
					blocks.remove(bluck)

				lenghts = len(blocks)

			if lenghts == length:
				origin = False
			else:
				pass



		print(len(blocks))
		if len(blocks) > 0:
			backup = reFetch(driver)

			for inds, secure in enumerate(backup):
				print("index", inds)
				#texts = secure.text

				try:

					texts = secure.text
					texts = texts.split('\n')
					disc = texts[0]
					summary = texts[1]

					reveal = secure.find_element_by_class_name("buy").click()
					time.sleep(15)
					try:
						codeBlock = driver.find_element_by_class_name("code-box").text
					except:
						driver.switch_to.window(driver.window_handles[0])
						codeBlock = driver.find_element_by_class_name("code-box").text


					codeBlock = codeBlock.split('\n')
					couponCode = codeBlock[0]

					print("fetching code...")
					print(couponCode)

					actions = ActionChains(driver)
					actions.send_keys(Keys.ESCAPE).perform()


					response = saveToCloud(firm, company, disc, summary, couponCode, disc_type)
					print(response)

				except Exception as error:
					
					print("...failed!")

					backup = reFetch(driver)

					element = backup[inds]

					texts = element.text
					texts = texts.split('\n')

					disc = texts[0]
					summary = texts[1]
					
					reveal = element.find_element_by_class_name("buy").click()
					
					time.sleep(15)
					try:
						codeBlock = driver.find_element_by_class_name("code-box").text
					except:
						driver.switch_to.window(driver.window_handles[0])
						codeBlock = driver.find_element_by_class_name("code-box").text

					codeBlock = codeBlock.split('\n')
					couponCode = codeBlock[0]

					print(couponCode)

					actions = ActionChains(driver)
					actions.send_keys(Keys.ESCAPE).perform()

					response = saveToCloud(firm, company, disc, summary, couponCode, disc_type)
					print(response)


					pass






def reFetch(driver):
	backup = []
	

	driver.refresh()
	backs = driver.find_elements_by_class_name("offerstrip")
	
	
	for data in backs:
		if 'Reveal Code' in data.text:
			backup.append(data)
			
		else:
			pass

	print(len(backup))
	return backup







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
	print("Calling OptimizedOffer python file")
	time.slee(5)
	
	driver = chrome_drive()
	driver = get_data(driver)
	driver.close()