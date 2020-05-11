#California Kitchen Pizza
#2nd trial

import pprint 
import requests
from bs4 import BeautifulSoup
import json










from flask_pymongo import PyMongo
from flask import Flask
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://devtotti:jankulovski@newclustera-c85ej.mongodb.net/pizzas?retryWrites=true&w=majority"
mongo = PyMongo(app)








pp = pprint.PrettyPrinter()

def crawl_exctract(url, firm, website):
    #names = []
    cp = "Get offers on website and stores"
    #url = "https://www.offers.com/california-pizza-kitchen/"
    #url = "https://www.offers.com/sbarro/"

    url = str(url)

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    con = soup.findAll("div", {"id":"offercontainer-2"}, "data-category")

    #firm = "cpkPizza"  #california_pizza_kitchen
    firm = str(firm)
    #print(firm)

    #website = "https://www.cpk.com/"
    website = str(website)
    #print(website)

    #econ1 = soup.select("div", {"class": "offerstrip card   positioned"})
    #print(econ)
    for econ in con:
        d  = econ.select("p")
        for ed in d:
            ed = str(ed.text)
                #print((ed))

            if ed == str(ed):
                discType = "SALES & OFFERS"
                cp = "Get Offers on website and stores"

            else:
                discType = "COUPON"
                cp = cp
                #print(discType)


        x = econ.select("h3", {"class":"name"})
            #print(x)

        for item in x:

            if len(item["class"]) != 1:
                continue;

            else:
                for z in item:
                    p = str(z)
                    p = p.replace("\n","").replace('\"',"")
                    #print((p))
                

            data = {"company":firm, "websiteName":website, "pizzaSummary":p, "discount":ed, "couponCode":cp , "discountType":discType}


            db = mongo.db.coupons

            count = []

            for field in db.find():
                if str(field['company']) == firm and str(field['websiteName']) == website and str(field['pizzaSummary']) == p and str(field['discount']) == ed and str(field['couponCode']) == cp and str(field['discountType']) == discType:
                    count.append(1)

                else: pass


            if len(count) > 0:
                print("Data exists in database")

            else:
                #data = {"company":firm, "websiteName":website, "pizzaSummary":p, "discount":ed, "couponCode":cp , "discountType":discType}
                

                try:
                    save = db.insert_one(data)

                    print("Data saved Successfully!")

                    response = "Seccess!"
                    return response

                except Exception as error:
                    print("Error saving into database: "+str(error))
                    response = "Failed!"
                    return response


    





