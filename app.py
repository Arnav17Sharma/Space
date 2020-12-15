import requests
import json
from nasa import get_data, get_images

from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/', methods=['GET',"POST"])
def home():
	data, lst = get_data()
	return render_template('index.html', data=data, lst=lst)

# @app.route('/images')
# def images():
# 	return render_template('images.html', data=get_images())



if __name__ == '__main__':
	app.run(debug=True)