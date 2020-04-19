from flask_pymongo import PyMongo
from flask import Flask


try:
	app = Flask(__name__)
	app.config["MONGO_URI"] = "mongodb+srv://devtotti:jankulovski@newclustera-c85ej.mongodb.net/pizzas?retryWrites=true&w=majority"
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
			

			companyName = str(field['websiteName'])
			summary = str(field['pizzaSummary'])
			discount = str(field['discount'])
			coupon = str(field['couponCode'])
			discountType = str(field['discountType'])

			print("company_url:"+companyName, "coupons:"+coupon)

			data = {"websiteName":companyName, "pizzaSummary": summary, "discount":discount, "couponCode":coupon, "discountType":discountType}
			database.append(data)

	
	except Exception as error:
		print("Collections retrieval failed!: ")
		



	return database



#queryDB()
