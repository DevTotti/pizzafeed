from flask_pymongo import PyMongo
from flask import Flask


try:
	app = Flask(__name__)
	#app.config["MONGO_URI"] = "mongodb+srv://devtotti:jankulovski@newclustera-c85ej.mongodb.net/pizzas?retryWrites=true&w=majority"
	app.config["MONGO_URI"] = "mongodb+srv://michael:Lagos12#@cluster0-lnbg3.mongodb.net/pizzas?retryWrites=true&w=majority"
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

