from flask import Flask, request, render_template, redirect, url_for, jsonify
from sklearn.externals import joblib
import pickle
import random

app = Flask(__name__)

@app.route('/')
def my_form():
 	return render_template('prediction.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # data = request.get_json()
            years_of_experience = float(request.form['years'])
            lin_reg = joblib.load("python_lin_reg_model.pkl")
        except ValueError:
            return jsonify("Please enter a number.")
        # return 'Your years of experience is %s' % years_of_experience
        # return jsonify(lin_reg.predict(years_of_experience).tolist())
        salary = int(lin_reg.predict(years_of_experience))	
        return 'Your expected salary is: %s' % salary



