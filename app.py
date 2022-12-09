from flask import Flask, request, render_template

from model import Model

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def stroke_form():
    return render_template('stroke.html')


@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        model = Model("forest_regression")
        data = model.preprocess(request.form)
        result = 100 * model.predict(data)
        res_success = True
        return render_template('stroke.html',
                               res_success=res_success,
                               name=request.form['name'],
                               result=result)
    return "<p>Something Wrong!</p>"
