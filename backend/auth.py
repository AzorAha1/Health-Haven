# from collections.abc import Sequence
# from typing import Any, Mapping
# from flask_wtf import FlaskForm
# from app import User
# from wtforms import StringField, PasswordField, EmailField, SubmitField, DateField, IntegerField
# from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

# class RegisterPatient(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)], render_kw={'class': 'design-field'})
#     email = EmailField(label='Email', validators=[DataRequired(), Email()], render_kw={'class': 'design-field'})
#     password = PasswordField(label='Password', validators=[DataRequired()],render_kw={'class': 'design-field'})
#     dob = DateField(label='Date of birth')
#     phonenum = IntegerField(label='Phone Number')
#     confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')],render_kw={'class': 'design-field'})
#     submit = SubmitField(label='Submit',render_kw={'class': 'submit-design'})

    # def validate_email(self, email):
    #     """this method will check if the email is already used by another user"""
    #     email = User.query.filter_by(email=email).first()

    #     if email:
    #         raise ValidationError(f'{email} already exists try another one')

    # def validate_user(self, username):
    #     """this method will check if username is already taken"""
    #     username = User.query.filter_by(username=username).first()
    #     if username:
    #         raise ValidationError(f'{username} is taken try another one')

        

# class LoginPatient(FlaskForm):
#     email = EmailField(label='Email', validators=[DataRequired(), Email()], render_kw={'class': 'design-field'})
#     password = PasswordField(label='Password', validators=[DataRequired()], render_kw={'class': 'design-field'})
#     submit = SubmitField(label='Login', render_kw={'class': 'submit-design'})