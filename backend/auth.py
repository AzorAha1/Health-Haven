from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, EqualTo

class RegisterPatient(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()], render_kw={'class': 'design-field'})
    email = EmailField(label='Email', validators=[DataRequired(), Email()], render_kw={'class': 'design-field'})
    password = PasswordField(label='Password', validators=[DataRequired()],render_kw={'class': 'design-field'})
    dob = DateField(validators=[DataRequired()], label='Date of birth')
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')],render_kw={'class': 'design-field'})
    submit = SubmitField(label='Submit',render_kw={'class': 'submit-design'})

class LoginPatient(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email()], render_kw={'class': 'design-field'})
    password = PasswordField(label='Password', validators=[DataRequired()], render_kw={'class': 'design-field'})
    submit = SubmitField(label='Login', render_kw={'class': 'submit-design'})