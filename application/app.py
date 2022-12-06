from flask import Flask, request, render_template

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
        gender = request.form['gender']
        age = request.form['age']
        # is_hypertension = request.form['isHypertension']
        # has_heart_disease = request.form['hasHeartDisease']
        # is_married = request.form['isMarried']
        # work_type = request.form['workType']
        # residence_type = request.form['residenceType']
        # glucose_level = request.form['glucoseLevel']
        # body_mass_index = request.form['bodyMassIndex']
        # smoke_status = request.form['smokeStatus']

        print(gender)
        print(age)
        res = "You have stroke"
        res_success = True
        return render_template('stroke.html', gender=gender, age=age, res_success=res_success)
    return "<p>Something Wrong!</p>"
