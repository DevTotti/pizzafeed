from flask import Flask, jsonify, request, render_template
from datetime import datetime
from fetchData import *
import schedule as sc
from data import *


app = Flask(__name__)


@app.route("/fetch", methods = ["GET"])
def fetchData():
	response = queryDB()
	response = {"response": response}

	return jsonify(response)



@app.route('/', methods = ["GET"])
def index():

	sc.every(30).minutes.do(main)

	while True:
		sc.run_pending()
		time.sleep(5)


if __name__ == "__main__":
	app.run(debug = True, port = 5000)



	
