import time
import schedule

from flask_pymongo import PyMongo
from flask import Flask
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://devtotti:jankulovski@newclustera-c85ej.mongodb.net/pizzas?retryWrites=true&w=majority"
mongo = PyMongo(app)




def job():
	print("I'm working")
	runJob()

def runJob():
	print("He's working")
	saveToCloud("a","b","c","d","e")


def saveToCloud(ada, bada, cada, dada, fada):
	db = mongo.db.coupons


	website = str(ada)
	discount = str(bada)
	summary = str(cada)
	code = str(dada)
	discountType = str(fada)

	data = {"websiteName":website, "pizzaSummary": summary, "discount":discount, "couponCode":code, "discountType":discountType}

	try:
		save = db.insert_one(data)

		print("Data saved Successfully!")

		response = "Seccess!"

	except Exception as error:
		print("Error saving into database: "+str(error))
		response = "Failed!"


	return response





schedule.every(1).minutes.do(job)


while True:
	schedule.run_pending()
	time.sleep(1)
