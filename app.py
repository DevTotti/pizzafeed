from flask import Flask, jsonify, request, render_template
from datetime import datetime
from fetchData import *
import schedule as sc
from optimized import *
from optimizedOffer import *



app = Flask(__name__)


@app.route("/fetch", methods = ["GET", "POST"])
def fetchData():

	if request.method == 'GET':
		response = queryDB()
		response = {"response": response}

		return jsonify(response)

	elif request.method == 'POST':
		company = request.get_json()["company"]
		discountType =  request.get_json()["discountType"]
		category = request.get_json()["category"]
		category_type = request.get_json()["categoryType"]

		response = queryParams(company, discountType)

		if category == 'topping':

			response = {"response":response}

			feedback = toppingSort(response, category)

			feedback = feedback[category_type]

			feedback = {"response":feedback}

			return feedback

		elif category == 'size':

			response = {"response":response}

			feedback = toppingSort(response, category)

			feedback = feedback[category_type]

			feedback = {"response":feedback}

			return feedback

		else:

			feedback = {"message":"invalid category"}
		
		
		"""		if request.get_json()["page"] != "":
					page = request.get_json()["page"]
					response = paginate(page, response)
					response = {"response":response}
					return jsonify(response)

				else:
					response = {"response":response}
					return jsonify(response)"""


	else:
		return {
			"message":"invalid request"
		}
			

@app.route("/fetch/category", methods = ['POST'])
def categorize():
	if request.method == 'POST':
		category = request.get_json()['category']
		response = queryDB()

		response = {"response":response}

		if category == 'topping':

			feedback = toppingSort(response, category)

		elif category == 'size':

			feedback = sizesort(response, category)

		else:

			feedback = {"message":"invalid category"}

	else:

		feedback = {"message":"invalid api request"}


	return feedback




@app.route('/fetch/category/company', methods = ['POST'])
def categorizeCompany():
	if request.method == 'POST':
		category = request.get_json()['category']
		company = request.get_json()['comapny']

		resonse = queryCompany(company)
		response = {"response":response}

		if category == 'topping':

			feedback = toppingSort(response, category)

		elif category == 'size':

			feedback = toppingSort(response, category)

		else:

			feedback = {"message":"invalid category"}


	else:

		feedback = {"message":"invalid api request"}
			


	return feedback




@app.route('/admin/fetch/category/topping', methods = ['GET'])
def adminToppingCategory():
	if request.method == 'GET':
		category = "topping"
		response = queryDB()
		response = {"response":response}
		feedback = toppingSort(response, category)

		

	else:
		feedback = {"message":"invalid api request"}


	return feedback




@app.route('/admin/fetch/category/size', methods = ['GET'])
def adminSizeCategory():
	if request.method == 'GET':
		category = "size"
		response = queryDB()
		response = {"response":response}
		feedback = sizesort(response, category)

		

	else:

		feedback = {"message":"invalid api request"}


	return feedback






#never call this route if you're not an admin. You are basically going to break something"
@app.route('/fuckoff', methods = ["GET"])
def index():


	while True:
		
		main()
		time.sleep(90)
		major()
		time.sleep(1800)


if __name__ == "__main__":
	app.run(debug = True, port = 5000)



