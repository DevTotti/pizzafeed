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

		if ('one topping' or 'one-topping' or 'one-Topping' or 'one Topping' or '1-Topping' or '1 Topping' or '1-topping' or '1 topping') in summary:
			category = '1-Topping'
			data.update({"topping":category})
			oneTopping.append(data)
			pass

		elif ('two topping' or 'two-topping' or 'two-Topping' or 'two Topping' or '2-Topping' or '2 Topping' or '2-topping' or '2 topping') in summary :
			categoy = '2-Topping'
			data.update({"topping":category})
			twoTopping.append(data)
			pass

		elif ('three topping' or 'three-topping' or 'three-Topping' or 'three Topping' or '3-Topping' or '3 Topping' or '3-topping' or '3 topping') in summary:
			category = '3-Topping'
			data.update({"topping":category})
			threeTopping.append(data)
			pass

		elif ('four topping' or 'four-topping' or 'four-Topping' or 'four Topping' or '4-Topping' or '4 Topping' or '4-topping' or '4 topping') in summary:
			category = '4-Topping'
			data.update({"topping":category})
			fourTopping.append(data)
			pass

		elif ('five topping' or 'five-topping' or 'five-Topping' or 'five Topping' or '5-Topping' or '5 Topping' or '5-topping' or '5 topping') in summary:
			category = '5-Topping'
			data.update({"topping":category})
			fiveTopping.append(data)
			pass


		else:
			category = 'others'
			data.update({"topping":category})
			others.append(data)
			pass


	feedback = {
		"oneTopping":oneTopping,
		"twoTopping":twoTopping,
		"threeTopping":threeTopping,
		"fourTopping":fourTopping,
		"fiveTopping":fiveTopping,
		"otherTopping":others
		}


	return feedback















