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


	

	db = mongo.db.coupons


	count = []
	for field in db.find():

		if str(field['company']) == firm and str(field['websiteName']) == wn and str(field['pizzaSummary']) == p_typ and str(field['discount']) == price and str(field['couponCode']) == cp and str(field['discountType']) == "COUPON":
			count.append(1)

		else:
			pass

	if len(count) > 0:
		print("Data exists in database")

	else:
		data = {"company":firm, "websiteName":wn, "pizzaSummary":p_typ,  "discount":price,  "couponCode":cp, "discountType":"COUPON"}

		try:
			save = db.insert_one(data)

			print("Data saved Successfully!")

			response = "Seccess!"
			return response

		except Exception as error:
			print("Error saving into database: "+str(error))
			response = "Failed!"
			return response





#marcoPizza()




