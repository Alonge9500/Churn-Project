from flask import Flask,render_template,request,redirect,url_for
from flask_wtf import CSRFProtect
from forms import PredictForm
import pickle
import os
import numpy as np

feature_scaler_path = os.path.join(os.path.dirname(__file__), '..', 'notebook', 'feature_scaler.pkl')
classifier_path = os.path.join(os.path.dirname(__file__), '..', 'notebook', 'churn_classifier.pkl')


with open(feature_scaler_path,'rb')as f:
    scaler = pickle.load(f)

with open(classifier_path,'rb')as y:
    classifier = pickle.load(y)


app = Flask(__name__)
app.secret_key = b'flyftfrhefguygdduylhutfrtfk'
csrf = CSRFProtect(app)


@app.route("/", methods=['GET','POST'])
def home():
    
    form = PredictForm()
    if form.validate_on_submit():
        gender = int(form.gender.data)
        seniorcit = int(form.seniorcit.data)
        partner = int(form.partner.data)
        tenure = int(form.tenure.data)
        dependents = int(form.dependents.data)
        phoneserv = int(form.phoneserv.data)
        papperlessbill = int(form.papperlessbill.data)
        mutiplelines = int(form.mutiplelines.data)
        internetserv = int(form.internetserv.data)
        onlinesecurity = int(form.onlinesecurity.data)
        onlinebackup = int(form.onlinebackup.data)
        deviceprotect = int(form.deviceprotect.data)
        techsupport = int(form.techsupport.data)
        streamingtv = int(form.streamingtv.data)
        streammov = int(form.streammov.data)
        contract = int(form.contract.data)
        paymentmethod = int(form.paymentmethod.data)
        monthsub = float(form.monthsub.data)
        totalsub = float(form.totalsub.data)
        
        data = np.array([seniorcit,tenure,monthsub,
                totalsub,mutiplelines,internetserv,
                onlinesecurity,onlinebackup,deviceprotect,
                techsupport,streamingtv,streammov,
                contract,paymentmethod,gender,
                partner,dependents,phoneserv,
                papperlessbill
                ])
        
        
        data = data.reshape(1,-1)
        data = scaler.transform(data)
        
        
        
        prediction=classifier.predict_proba(data)[0]
        
        print(prediction)
        return redirect(url_for('result',prediction=prediction))
        
    else:
        return render_template('home.html',form=form)


@app.route("/result")
def result():
    prediction = (request.args.get('prediction')).split(' ')
    pred_yes = float(prediction[0][1:]) * 100
    pred_no = float(prediction[1][:-2]) * 100
    
    prediction = [pred_yes,pred_no]
    print(prediction)
    return render_template('result.html', pred=prediction)
if __name__ == "__main__":
    app.run(debug=True)
    
    