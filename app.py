from flask import Flask,render_template,request,jsonify
import flask_sqlalchemy 
import xgboost as xgb
import numpy as np
import joblib
import numpy as np
app = Flask(__name__)



    
model = joblib.load("models/model.joblib")

@app.route("/",methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        age = request.form.get('age')
        sex = request.form.get('sex')
        bmi = request.form.get('bmi')
        bp = request.form.get('bp')
        s1 = request.form.get('s1')
        s2 = request.form.get('s2')
        s3 = request.form.get('s3')
        s4 = request.form.get('s4')
        s5 = request.form.get('s5')
        s6 = request.form.get('s6')
        to_predict = np.array([age,sex,bmi,bp,s1,s2,s3,s4,s5,s6]).astype(float)
        to_predict = to_predict.reshape(1,10)
        to_predict = (to_predict - np.mean(to_predict,axis=0)) / np.std(to_predict,axis=0)
        #We check for seing whether has fit or predict attribute
        print(type(model))
        print(hasattr(model,'fit'))
        print(hasattr(model,'predict'))
        print(to_predict.shape,to_predict) 
        try:
            y_predict = model.predict(to_predict)
            return f"<div><h3 class='text-error'>Prediction of the Diabetes Progression:<span class='text-primary'> {y_predict}</span></h3><div class='progress' role='progressbar' aria-label='Diabete Progression' aria-valuenow={y_predict} aria-valuemax='350' aria-valuemin='25'><div class='progress-bar bg-primary' style='width: 10%;height:100px'></div></div></div>"
        except Exception as e: # In case of error it will print it for us
            print(e)
            return render_template('error.html')
    else:
        return render_template('index.html')

if __name__ ==  "__name__":
    app.run(debug=True)