import pprint
import requests
from bs4 import BeautifulSoup
import json
import re


from flask_pymongo import PyMongo
from flask import Flask
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://devtotti:jankulovski@newclustera-c85ej.mongodb.net/pizzas?retryWrites=true&w=majority"
mongo = PyMongo(app)





def ciciPizza():
    firm = "cicis"
    url = "https://www.cicis.com/offers/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    wn = soup.title.string
    #print (wn) #Site Name

    results = soup.find_all("div", {"class": "theme-content false"})
    #print(results)

    for item in results:
    
        cp = item.find_all("div", {"class": "mk-text-block"})
        #pprint.pprint(cp)

        for e in cp:
            #cp = e.find_all("p", string = re.compile('^ENTER CODE.*' , re.IGNORECASE))
        
            wn = url[:21]
        
            try:
                cp = e.contents[2].text
                if cp == "":
                    discType = "SALES & OFFERS"
                    cp = "Get offers on website and stores"
                else:
                    discType = "COUPON"
                    cp = cp
            except:
                pass
        
            try:
                p_typ = e.contents[1].text
            except:
                pass


            data = {"company":firm, "websiteName":wn, "pizzaSummary":p_typ, "couponCode":cp, "discount":"", "discountType":discType}

            db = mongo.db.coupons

            try:
                save = db.insert_one(data)

                print("Data saved Successfully!")

                response = "Seccess!"

            except Exception as error:
                print("Error saving into database: "+str(error))
                response = "Failed!"

    return response
        

