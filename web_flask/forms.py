import os
from flask_wtf import FlaskForm  
from wtforms import validators, ValidationError  
from wtforms import IntegerField, DecimalField, SubmitField, RadioField, SelectField
import pickle




class PredictForm(FlaskForm):
    gender = RadioField('Select Gender',choices=[(1,'Male'), (0,'Female')], validators=[validators.DataRequired()])
    seniorcit = RadioField('Is customer a senior citizen',choices=[(1,'Yes'), (0,'No')], validators=[validators.DataRequired()])
    partner = RadioField('Does customer have a Partner?',choices=[(1,'Yes'), (0,'No')], validators=[validators.DataRequired()])
    tenure = IntegerField('How many Month since customer joined',validators=[validators.DataRequired()])
    dependents = RadioField('Does customer have dependents?',choices=[(1,'Yes'), (0,'No')], validators=[validators.DataRequired()])
    phoneserv = RadioField('Does customer have phone service?',choices=[(1,'Yes'), (0,'No')], validators=[validators.DataRequired()])
    papperlessbill = RadioField('Does customer run a Paperless Billing?',choices=[(1,'Yes'), (0,'No')], validators=[validators.DataRequired()])
    mutiplelines = SelectField('Does customer run MultipleLines',choices=[(1,'No Phone service'), (0,'No'),(2,'Yes')], validators=[validators.DataRequired()])
    internetserv = SelectField('What type of internet service does the customer have',choices=[(1,'Fiber Optic'), (0,'DSL'),(2,'NO')], validators=[validators.DataRequired()])
    onlinesecurity = SelectField('Does customer have Online security',choices=[(1,'No internet service'), (0,'No'),(2,'Yes')], validators=[validators.DataRequired()])
    onlinebackup = SelectField('Does customer have Online Backup',choices=[(1,'No internet service'), (0,'No'),(2,'Yes')], validators=[validators.DataRequired()])
    deviceprotect = SelectField('Does customer have device protection',choices=[(1,'No internet service'), (0,'No'),(2,'Yes')], validators=[validators.DataRequired()])
    techsupport = SelectField('Does customer have tech support',choices=[(1,'No internet service'), (0,'No'),(2,'Yes')], validators=[validators.DataRequired()])
    streamingtv = SelectField('Does customer stream TV',choices=[(1,'No internet service'), (0,'No'),(2,'Yes')], validators=[validators.DataRequired()])
    streammov = SelectField('Does customer stream Movies',choices=[(1,'No internet service'), (0,'No'),(2,'Yes')], validators=[validators.DataRequired()])
    contract = SelectField('Contract Type',choices=[(1,'One Year'), (0,'Month to Month'),(2,'Two Year')], validators=[validators.DataRequired()])
    paymentmethod = SelectField('Payment Method',choices=[(1,'Credit Card(automatic)'), (0,'Bank Transfer(automatic)'),(2,'Electronic check'),(3,'Mailed Check')], validators=[validators.DataRequired()])
    monthsub = DecimalField('Monthly Subscription', validators=[validators.DataRequired(), validators.NumberRange(min=0.01)])
    totalsub = DecimalField('Total Subscription', validators=[validators.DataRequired(), validators.NumberRange(min=0.01)])
    submit = SubmitField('Submit')


    
    
    
     
    
    
    
    