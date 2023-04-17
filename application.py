import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

## import ridge regression model pickle file

ridge_model = pickle.load(open('models/ridge.pkl','rb'))
standard_scaler = pickle.load(open('models/scale.pkl','rb'))

## Route for home page

@app.route("/")
def index():
    return (render_template("index.html"))

@app.route("/predictdata",methods = ['GET','POST'])
def predict_datapoint():
    if (request.method == 'POST'):
        temp    = float(request.form.get('Temperature'))
        rh      = float(request.form.get('RH'))
        ws      = float(request.form.get('Ws'))
        rain    = float(request.form.get('Rain'))
        ffmc    = float(request.form.get('FFMC'))
        dmc     = float(request.form.get('DMC'))
        isi     = float(request.form.get('ISI'))
        classes = float(request.form.get('Classes'))
        region  = float(request.form.get('Region'))

        new_scaled_data = standard_scaler.transform([[temp,rh,ws,rain,ffmc,dmc,isi,classes,region]])
        predict = ridge_model.predict(new_scaled_data)

        return render_template('home.html' , result = predict[0])

    else:
        return render_template("home.html")    

if __name__=="__main__":
    app.run(host="0.0.0.0")
