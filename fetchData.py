from flask_pymongo import PyMongo
from flask import Flask


try:
	app = Flask(__name__)
	#app.config["MONGO_URI"] = "mongodb+srv://devtotti:jankulovski@newclustera-c85ej.mongodb.net/pizzas?retryWrites=true&w=majority"
	app.config["MONGO_URI"] = "mongodb+srv://michael:Lagos12#@cluster0-3gczm.mongodb.net/pizzas?retryWrites=true&w=majority"
	mongo = PyMongo(app)
	print("Connection Successful!")

except Exception as error:
	print("Error connecting to database: "+str(error))



def queryDB():
	database = []
	try:
		db = mongo.db.coupons
		print("Collections retrieval Successful! ")



		for field in db.find():
			
			firm = str(field['company'])
			companyName = str(field['websiteName'])
			summary = str(field['pizzaSummary'])
			discount = str(field['discount'])
			coupon = str(field['couponCode'])
			discountType = str(field['discountType'])

			print("company_url:"+companyName, "coupons:"+coupon)

			data = {"company":firm, "websiteName":companyName, "pizzaSummary": summary, "discount":discount, "couponCode":coupon, "discountType":discountType}
			database.append(data)

	
	except Exception as error:
		print("Collections retrieval failed!: "+str(error))
		



	return database



def queryParams(firm, discountType):
	database = []
	company = str(firm)
	discType = str(discountType)
	try:
		db = mongo.db.coupons
		print("Collections retrieval Successful! ")

		for field in db.find():

			if str(field['company']) == company and str(field['discountType']) == discType:
				firm = str(field['company'])
				companyName = str(field['websiteName'])
				summary = str(field['pizzaSummary'])
				discount = str(field['discount'])
				coupon = str(field['couponCode'])
				discountType = str(field['discountType'])

				print("company_url:"+companyName, "coupons:"+coupon)

				data = {"company":firm, "websiteName":companyName, "pizzaSummary": summary, "discount":discount, "couponCode":coupon, "discountType":discountType}
				database.append(data)

			else:
				pass

	
	

	except Exception as error:
		print("Collections retrieval failed!: "+str(error))


	return database



def paginate(page, data):
	#algorithm for the pagination
	print("Paginating")
	database = data
	number = int(page) - 1
	start = (number*5)
	stop = (start + 5)
	data = database[start:stop]

	response = data
	
	return response


#queryDB()


def toppingSort(response, category):
	print("categorizing now...")

	oneTopping = []
	twoTopping = []
	threeTopping = []
	fourTopping = []
	fiveTopping = []
	others = []

	database = response

	response = database['response']

	for data in response:
		summary = data['pizzaSummary']
		print(data)


		if 'one topping' in summary :
			category = '1-Topping'
			
			print(data)
			oneTopping.append(data)
			pass

		elif 'one-topping' in summary:
			category = '1-Topping'
			
			print(data)
			oneTopping.append(data)
			pass

		elif 'one-Topping' in summary:
			category = '1-Topping'
			
			print(data)
			oneTopping.append(data)
			pass

		elif 'one Topping' in summary :
			category = '1-Topping'
			
			print(data)
			oneTopping.append(data)	
			pass

		elif '1-Topping' in summary :
			category = '1-Topping'
			
			print(data)
			oneTopping.append(data)	
			pass

		elif '1 Topping' in summary :
			category = '1-Topping'
			
			print(data)
			oneTopping.append(data)		
			pass

		elif '1-topping' in summary :
			category = '1-Topping'
			
			print(data)
			oneTopping.append(data)	
			pass	
				
		elif '1 topping' in summary:
			category = '1-Topping'
			
			print(data)
			oneTopping.append(data)
			pass

		elif 'two topping' in summary:
			categoy = '2-Topping'
			
			print(data)
			twoTopping.append(data)
			pass

		elif 'two-topping' in summary :
			categoy = '2-Topping'
			
			print(data)
			twoTopping.append(data)
			pass

		elif 'two-Topping' in summary :
			categoy = '2-Topping'
			
			print(data)
			twoTopping.append(data)
			pass

		elif 'two Topping' in summary :
			categoy = '2-Topping'
			
			print(data)
			twoTopping.append(data)
			pass

		elif '2-Topping' in summary :
			categoy = '2-Topping'
			
			print(data)
			twoTopping.append(data)
			pass

		elif '2 Topping' in summary :
			categoy = '2-Topping'
			
			print(data)
			twoTopping.append(data)
			pass

		elif '2-topping' in summary :
			categoy = '2-Topping'
			
			print(data)
			twoTopping.append(data)
			pass

		elif '2 topping' in summary :
			categoy = '2-Topping'
			
			print(data)
			twoTopping.append(data)
			pass


		elif 'three topping' in summary : 
			category = '3-Topping'
			
			print(data)
			threeTopping.append(data)
			pass

		elif 'three-topping' in summary :
			category = '3-Topping'
			
			print(data)
			threeTopping.append(data)
			pass

		elif 'three-Topping' in summary :
			category = '3-Topping'
			
			print(data)
			threeTopping.append(data)
			pass

		elif 'three Topping' in summary :
			category = '3-Topping'
			
			print(data)
			threeTopping.append(data)
			pass

		elif '3-Topping' in summary :
			category = '3-Topping'
			
			print(data)
			threeTopping.append(data)
			pass

		elif '3 Topping' in summary :
			category = '3-Topping'
			
			print(data)
			threeTopping.append(data)
			pass

		elif '3-topping' in summary :
			category = '3-Topping'
			
			print(data)
			threeTopping.append(data)
			pass

		elif '3 topping' in summary:
			category = '3-Topping'
			
			print(data)
			threeTopping.append(data)
			pass

		elif 'four topping' in summary : 
			category = '4-Topping'
			
			print(data)
			fourTopping.append(data)
			pass

		elif 'four-topping' in summary :
			category = '4-Topping'
			
			print(data)
			fourTopping.append(data)
			pass

		elif 'four-Topping' in summary :
			category = '4-Topping'
			
			print(data)
			fourTopping.append(data)
			pass

		elif 'four Topping' in summary :
			category = '4-Topping'
			
			print(data)
			fourTopping.append(data)
			pass

		elif '4-Topping' in summary :
			category = '4-Topping'
			
			print(data)
			fourTopping.append(data)
			pass

		elif '4 Topping' in summary :
			category = '4-Topping'
			
			print(data)
			fourTopping.append(data)
			pass

		elif '4-topping' in summary :
			category = '4-Topping'
			
			print(data)
			fourTopping.append(data)
			pass

		elif '4 topping' in summary:
			category = '4-Topping'
			
			print(data)
			fourTopping.append(data)
			pass


		elif 'five topping' in summary : 
			category = '5-Topping'
			
			print(data)
			fiveTopping.append(data)
			pass

		elif 'five-topping' in summary :
			category = '5-Topping'
			
			print(data)
			fiveTopping.append(data)
			pass

		elif 'five-Topping' in summary :
			category = '5-Topping'
			
			print(data)
			fiveTopping.append(data)
			pass

		elif 'five Topping' in summary :
			category = '5-Topping'
			
			print(data)
			fiveTopping.append(data)
			pass

		elif '5-Topping' in summary :
			category = '5-Topping'
			
			print(data)
			fiveTopping.append(data)
			pass

		elif '5 Topping' in summary :
			category = '5-Topping'
			
			print(data)
			fiveTopping.append(data)
			pass

		elif '5-topping' in summary :
			category = '5-Topping'
			
			print(data)
			fiveTopping.append(data)
			pass

		elif '5 topping' in summary:
			category = '5-Topping'
			
			print(data)
			fiveTopping.append(data)
			pass



		else:
			category = 'others'
			
			print(data)
			others.append(data)
			pass


	feedback = {
		"1":oneTopping,
		"2":twoTopping,
		"3":threeTopping,
		"4":fourTopping,
		"5":fiveTopping,
		"otherTopping":others
		}


	return feedback




def sizesort(response, category):

	print("categorizing now...")

	large = []
	medium = []
	small = []
	xlarge = []
	others = []

	database = response

	response = database['response']

	for data in response:
		summary = data['pizzaSummary']

		if 'large' in summary: 
			category = 'Large'
			data.update({"size":category})
			large.append(data)
			pass

		elif 'Large' in summary:
			category = 'Large'
			data.update({"size":category})
			large.append(data)
			pass

		elif 'big' in summary:
			category = 'Large'
			data.update({"size":category})
			large.append(data)
			pass


		elif 'medium' in summary:
			categoy = 'medium'
			data.update({"size":category})
			medium.append(data)
			pass

		elif 'mid' in summary:
			categoy = 'medium'
			data.update({"size":category})
			medium.append(data)
			pass

		elif 'intermediate' in summary:
			categoy = 'medium'
			data.update({"size":category})
			medium.append(data)
			pass


		elif 'small' in summary:
			category = 'small'
			data.update({"size":category})
			small.append(data)
			pass

		elif 'little' in summary :
			category = 'small'
			data.update({"size":category})
			small.append(data)
			pass

		elif 'tiny' in summary:
			category = 'small'
			data.update({"size":category})
			small.append(data)
			pass



		elif 'extralarge' in summary :
			category = 'extralarge'
			data.update({"size":category})
			xlarge.append(data)
			pass

		elif 'extra large' in summary :
			category = 'extralarge'
			data.update({"size":category})
			xlarge.append(data)
			pass

		elif 'xtralarge' in summary :
			category = 'extralarge'
			data.update({"size":category})
			xlarge.append(data)
			pass

		elif  'xtra large' in summary:
			category = 'extralarge'
			data.update({"size":category})
			xlarge.append(data)
			pass
						

		else:
			category = 'others'
			data.update({"size":category})
			others.append(data)
			pass


	feedback = {
		"extralarge":xlarge,
		"large":large,
		"medium":medium,
		"small":small,
		"otherSize":others
		}


	return feedback


def sortPreference(database):
	sortedData = database
	stuffed = []
	regular = []
	others = []

	response = sortedData['response']

	for data in sortedData:
		summary = data['pizzaSummary']

		if "stuffed crust" in summary:
			data.update({"preference":"stuffed_crust"})
			stuffed.append(data)

		elif "regular" in summary:
			data.update({"preference":"regular"})
			stuffed.append(data)

		else:
			data.update({"preference":"other"})
			others.append(data)


	feedback = {
		"stuffed_crust":stuffed,
		"regular":regular,
		"others":others
	}



	return feedback





def queryCompany(company):
	database = []
	company = str(company)
	
	try:
		db = mongo.db.coupons
		print("Collections retrieval Successful! ")

		for field in db.find():

			if str(field['company']) == company:
				firm = str(field['company'])
				companyName = str(field['websiteName'])
				summary = str(field['pizzaSummary'])
				discount = str(field['discount'])
				coupon = str(field['couponCode'])
				discountType = str(field['discountType'])

				print("company_url:"+companyName, "coupons:"+coupon)

				data = {"company":firm, "websiteName":companyName, "pizzaSummary": summary, "discount":discount, "couponCode":coupon, "discountType":discountType}
				database.append(data)

			else:
				pass




	except Exception as error:
		print("Collections retrieval failed!: "+str(error))


	return database









