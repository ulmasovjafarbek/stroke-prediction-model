from flask import Flask, request, render_template

from model import Model
import numpy as np

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Home Page!</p>"


@app.route('/app', methods=['GET', 'POST'])
def stroke_form():
    return render_template('stroke.html')


@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        model = Model("forest_regression")
        data = model.preprocess(request.form)
        result = model.predict(data)
        print(result)
        res_success = True
        return render_template('stroke.html',
                               res_success=res_success,
                               result=result)
    return "<p>Something Wrong!</p>"
