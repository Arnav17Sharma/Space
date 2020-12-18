import requests
import json
from nasa import get_data, get_images
from spacex import rocket_list

from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/', methods=['GET', "POST"])
def home():
    data, lst = get_data()
    return render_template('index.html', data=data, lst=lst)


@app.route('/spacex')
def spacex():
    return render_template('spacex.html', data=rocket_list())


if __name__ == '__main__':
    app.run(debug=True)
