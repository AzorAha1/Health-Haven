from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class RegisterPatient(FlaskForm):
    username = StringField(label='username', validators=[DataRequired()])
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Submit')

class LoginPatient(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email()], render_kw={'class': 'design-field'})
    password = PasswordField(label='Password', validators=[DataRequired()], render_kw={'class': 'design-field'})
    submit = SubmitField(label='Login', render_kw={'class': 'submit-design'})