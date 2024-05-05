import os
from flask import Flask, render_template, request
from Models.model import Modelr
import pandas as pd

app = Flask(__name__)

# initialize the model
model = Modelr('trained_model/model.pkl')

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get feature values from form input
    superficy = float(request.form['superficy'])
    year_built = int(request.form['yearb'])
    num_bedrooms = int(request.form['no_bedrooms'])
    num_bathrooms = int(request.form['no_bathrooms'])
    grade = int(request.form['grade'])

    waterfront_values = request.form.getlist('waterfront')
    if 'yes' in waterfront_values:
        waterfront = 1
    else:
        waterfront = 0
    
    # predire
    features = [[ superficy, year_built, num_bedrooms, num_bathrooms, grade, waterfront]]
    prediction_list = model.predict(features)
    prediction_str = str(prediction_list).replace("]", "").replace("[", "").strip()
    prediction = round(float(prediction_str),2)

    
    return render_template('result.html', prediction=prediction)











if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)