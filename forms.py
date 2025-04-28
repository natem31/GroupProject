from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email')
    submit = SubmitField('Create Profile')

class CommitmentForm(FlaskForm):
    title = StringField('Commitment Title', validators=[DataRequired()])
    day_of_week = SelectField('Day of Week', choices=[('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thursday','Thursday'),('Friday','Friday'),('Saturday','Saturday'),('Sunday','Sunday')])
    start_time = TimeField('Start Time', validators=[DataRequired()])
    end_time = TimeField('End Time', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Class','Class'),('Practice','Practice'),('Lift','Lift'),('Meeting','Meeting'),('Other','Other')])
    submit = SubmitField('Add Commitment')
