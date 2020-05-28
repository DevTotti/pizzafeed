from flask import Flask, jsonify, request, render_template
from datetime import datetime
from fetchData import *
import schedule as sc
from optimized import *
from optimizedOffer import *
"""from data import *
from data1 import *"""


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
		response = queryParams(company, discountType)
		
		if request.get_json()["page"] != "":
			page = request.get_json()["page"]
			response = paginate(page, response)
			response = {"response":response}
			return jsonify(response)

		else:
			response = {"response":response}
			return jsonify(response)
			



@app.route('/fuckoff', methods = ["GET"])
def index():

	#sc.every(30).minutes.do(main)

	while True:
		#sc.run_pending()
		main()
		time.sleep(90)
		major()
		time.sleep(1800)


if __name__ == "__main__":
	app.run(debug = True, port = 5000)



