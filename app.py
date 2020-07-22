from flask import Flask, jsonify, request, render_template
from datetime import datetime
from flasgger import Swagger
from flasgger.utils import swag_from
from fetchData import *
import schedule as sc
from optimized import *
from optimizedOffer import *



app = Flask(__name__)
app.config['SWAGGER'] = {"title":"Swagger-UI", "version":2}

swagger_config = {
	"headers":[],
	"specs":[
		{
			"endpoint":"apispec_1",
			"route":"/apispec_1.json",
			"rule_filter":lambda rule: True,
			"model_filter": lambda tag: True,
		}
	],
	"static_url_path":"/flasgger_static",
	"swagger_ui":True,
	"specs_route":"/swagger/",
}

swagger = Swagger(app, config = swagger_config)


@app.route("/fetch", methods = ["GET", "POST"])
@swag_from("swagger_yml/swagger_config.yml", methods = ['POST'])
@swag_from("swagger_yml/swagger_config_get.yml", methods = ['GET'])
def fetchData():

	if request.method == 'GET':
		response = queryDB()
		response = {"response": response}

		return jsonify(response)

	elif request.method == 'POST':
		company = request.get_json()["company"]
		discountType =  request.get_json()["discountType"]
		topping = request.get_json()["topping"]
		size = request.get_json()["size"]
		#preference = request.get_json()["preferences"]

		response = queryParams(company, discountType)

		#if category == 'topping':
		category = "topping/size"

		response = {"response":response}

		feedback = toppingSort(response, category)

		feedback = feedback[topping]

		#response = {"response":feedback}

		#sortingpref = sortPreference(response)

		#feedback = sortingpref[preference]

		response = {"response":feedback}

		feedback = sizesort(response, category)

		feedback = feedback[size]

		#feedback = {"response":feedback}
		
		
		if request.get_json()["page"] != "":
			page = request.get_json()["page"]
			response = paginate(page, feedback)
			response = {"response":response}
			return jsonify(response)

		else:
			response = {"response":feedback}
			return jsonify(response)


	else:
		return {
			"message":"invalid request"
		}
			

@app.route("/fetch/category", methods = ['POST'])
@swag_from("swagger_yml/swagger_category_config.yml", methods = ['POST'])
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
@swag_from("swagger_yml/swagger_category_company_config.yml", methods = ['POST'])
def categorizeCompany():
	if request.method == 'POST':
		category = request.get_json()['category']
		company = request.get_json()['company']

		response = queryCompany(company)
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




@app.route('/admin/fetch/category/topping', methods = ['GET'])
@swag_from("swagger_yml/swagger_category_topping_config.yml", methods = ['GET'])
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
@swag_from("swagger_yml/swagger_category_size_config.yml", methods = ['GET'])
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



