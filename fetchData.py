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

		if 'one topping' in summary or 'one-topping' in summary or 'one-Topping' in summary or 'one Topping' in summary or '1-Topping' in summary or '1 Topping' in summary or '1-topping' in summary or '1 topping' in summary:
			category = '1-Topping'
			data.update({"topping":category})
			oneTopping.append(data)
			pass

		elif 'two topping' in summary or 'two-topping' in summary or 'two-Topping' in summary or 'two Topping' in summary or '2-Topping' in summary or '2 Topping' in summary or '2-topping' in summary or '2 topping' in summary :
			categoy = '2-Topping'
			data.update({"topping":category})
			twoTopping.append(data)
			pass

		elif 'three topping' in summary or 'three-topping' in summary or 'three-Topping' in summary or 'three Topping' in summary or '3-Topping' in summary or '3 Topping' in summary or '3-topping' in summary or '3 topping' in summary:
			category = '3-Topping'
			data.update({"topping":category})
			threeTopping.append(data)
			pass

		elif 'four topping' in summary or 'four-topping' in summary or 'four-Topping' in summary or 'four Topping' in summary or '4-Topping' in summary or '4 Topping' in summary or '4-topping' in summary or '4 topping' in summary:
			category = '4-Topping'
			data.update({"topping":category})
			fourTopping.append(data)
			pass

		elif 'five topping' in summary or 'five-topping' in summary or 'five-Topping' in summary or 'five Topping' in summary or '5-Topping' in summary or '5 Topping' in summary or '5-topping' in summary or '5 topping' in summary:
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
		1:oneTopping,
		2:twoTopping,
		3:threeTopping,
		4:fourTopping,
		5:fiveTopping,
		"otherTopping":others
		}


	return feedback




def sizesort(response, category):

	print("categorizing now...")

	large = []
	medium = []
	small = []
	others = []

	database = response

	response = database['response']

	for data in response:
		summary = data['pizzaSummary']

		if 'large' in summary or 'Large' in summary or 'big' in summary:
			category = 'Large'
			data.update({"size":category})
			large.append(data)
			pass

		elif 'medium' in summary or 'mid' in summary or 'intermediate' in summary :
			categoy = 'medium'
			data.update({"size":category})
			medium.append(data)
			pass

		elif 'small' in summary or 'little' in summary or 'tiny' in summary:
			category = 'small'
			data.update({"size":category})
			small.append(data)
			pass

		else:
			category = 'others'
			data.update({"size":category})
			others.append(data)
			pass


	feedback = {
		"large":large,
		"medium":medium,
		"small":small,
		"otherSize":others
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









