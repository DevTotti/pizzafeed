import requests
from bs4 import BeautifulSoup
import json




from flask_pymongo import PyMongo
from flask import Flask
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://devtotti:jankulovski@newclustera-c85ej.mongodb.net/pizzas?retryWrites=true&w=majority"
mongo = PyMongo(app)







def marcoPizza():
	firm = "marcosPizza"

	url = "https://www.marcos.com/"
	page = requests.get(url)

	soup = BeautifulSoup(page.content, 'html.parser')

	wn = soup.title.string
	print (wn) #Site Name


	results = soup.find("div", {"class": "m-deal m-deal-hero off50-m-deal unlimited-m-deal"})

	p_typ = results.find("h2", {"class": "hero-sub-heading"}).text    #pizza summary
	print(p_typ)

	price = results.find("img", {"class": "price-image unlimited-priceimg"})  #price discount
	price = price['alt']
	print(price)

	cp = results.find("h3", {"class": "promocode-text"}).text       #coupon Code
	print( cp)


	data = {"company":firm, "websiteName":wn, "pizzaSummary":p_typ,  "discount":price,  "couponCode":cp, "discountType":"coupon"}

	db = mongo.db.coupons

	try:
		save = db.insert_one(data)

		print("Data saved Successfully!")

		response = "Seccess!"

	except Exception as error:
		print("Error saving into database: "+str(error))
		response = "Failed!"


	return response



#marcoPizza()





