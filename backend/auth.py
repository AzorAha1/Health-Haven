from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class RegisterPatient(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Submit')

class LoginPatient(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')