from flask import Flask, render_template, url_for,redirect, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
import os
from flask_migrate import Migrate


from wtforms import StringField, PasswordField, EmailField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user

# Get the absolute path to the backend folder
backend_dir = os.path.abspath(os.path.dirname(__file__))
# # Set the database file path relative to the backend folder
db_file = os.path.join(backend_dir, 'health-haven.db')

# Update the database URI


app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/styles')
app.config['SECRET_KEY'] = 'd408adac2785c9429f66f099f0d2a4a4'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_file}'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://healthhaven_postgresql_9eiw_user:6i86UXkj2uD73hfGQ6o4WANJRNkxzqMu@dpg-cnvlmkqcn0vc73c8vgi0-a.oregon-postgres.render.com/healthhaven_postgresql_9eiw'
# postgres://healthhaven_postgresql_user:R4UVek96nE04g781udjBcwkrcUoYLkYG@dpg-cnveif2cn0vc73c82b00-a/healthhaven_postgresql


db = SQLAlchemy(app=app)
bcrypt = Bcrypt(app=app)
login_manager = LoginManager(app=app)
login_manager.init_app(app=app)
migrate = Migrate(app, db)

# load user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True, nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    dob = db.Column(db.DateTime, nullable=True)
    phonenum = db.Column(db.String(20), nullable=True)
    def __repr__(self):
        return f'the user id is {self.user_id}, the email is {self.email}, the username is {self.username}'
    
    def get_id(self):
        return str(self.user_id)

class Doctor(db.Model):
    doctor_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    specialty = db.Column(db.String(60), nullable=False)
    yearsofexperience = db.Column(db.Integer(), nullable=False)
    def __repr__(self):
        if self.yearsofexperience > 1:
            return f'Doctor {self.name} specializes in {self.specialty} and has {self.yearsofexperience} years in experience'
        elif self.yearsofexperience == 1:
            return f'Doctor {self.name} specializes in {self.specialty} and has {self.yearsofexperience} year in experience'
        else:
            return 'Not Qualified'
    

class Appointment(db.Model):
    __tablename__ = 'appointments'
    appointment_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.doctor_id'))

    user = db.relationship('User', backref=db.backref('appointments', lazy=True))
    doctor = db.relationship('Doctor', backref=db.backref('appointments', lazy=True))

    def __repr__(self):
        newdate = self.date.strftime('%d-%m-%Y')
        return f'Appointment with {self.doctor} requested on {newdate}, we will get back to you soon for the meetup date'


    
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """This brings a user to the home page of the app"""
    return render_template('home.html', title='Home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """This brings a user to the register page of the app"""
    form = RegisterPatient()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user_1 = User(username=form.username.data, email=form.email.data, dob=form.dob.data, phonenum=form.phonenum.data, password=hash_password)
        db.session.add(user_1)
        db.session.commit()
        flash(message=f'Account Successfully Created for {form.username.data} Now you can Login', category='success')
        print(f"User {form.username.data} added to the database")
        return redirect(url_for('login'))
    return render_template('register.html', title='Login', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """This brings a user to the login page of the app"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginPatient()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            print(form.email.data, form.password.data)
            login_user(user=user)
            print(form.email.data, form.password.data)
            return redirect(url_for('home'))    
        else:
            print('unsuccessful')
            flash(message=f'Login was unsuccessful check username or password', category='danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/about')
def about():
    """This brings a user to the about page of the app"""
    return render_template('about.html', title='Home')

@app.route('/search', methods=['GET'])
def search():
    """Returns information that matches the parameters"""
    specialization = request.args.get('specialization')
    
    if specialization == 'counselling':
        return render_template('specializations/counselling.html')
    elif specialization == 'general-medicine':
        return render_template('specializations/general-medicine.html')
    elif specialization == 'physiotherapy':
        return render_template('specializations/physiotherapy.html')
    elif specialization == 'dermatology':
        return render_template('specializations/dermatology.html')
    elif specialization == 'endocrinology':
        return render_template('specializations/endocrinology.html')
    elif specialization == 'dentistry':
        return render_template('specializations/dentistry.html')
    return render_template('search.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/setup_appointment', methods=['GET', 'POST'])
def setup_appointment():
    """set appointment"""
    doctors = Doctor.query.all()
    return render_template('setup_appointment.html', doctors=doctors)

@app.route('/my_appointments', methods=['GET', 'POST'])
def my_appointments():
    user_id = request.form.get('user_id')
    doctor_id = request.form.get('doctor_id')


    if not user_id or not doctor_id or  doctor_id == 'no choice':
        flash(message='Please Select a Doctor', category='danger')
        return redirect(url_for('setup_appointment'))
    else:
        my_appointments = Appointment(user_id=user_id, doctor_id=doctor_id)
        db.session.add(my_appointments)
        db.session.commit()
        flash('Appointment set with Doctor', category='success')
        return redirect(url_for('home'))
@app.route('/show_appointments/')
def show_appointments():
    if current_user.is_authenticated:
        user_id = current_user.get_id()
        appointments = Appointment.query.filter_by(user_id=user_id).all()
        return render_template('show_ap.html', appointments=appointments)
    else:
        return redirect(url_for('login'))
    
    


# forms 
class RegisterPatient(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)], render_kw={'class': 'design-field'})
    email = EmailField(label='Email', validators=[DataRequired(), Email()], render_kw={'class': 'design-field'})
    password = PasswordField(label='Password', validators=[DataRequired()],render_kw={'class': 'design-field'})
    dob = DateField(label='Date of birth')
    phonenum = IntegerField(label='Phone Number')
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')],render_kw={'class': 'design-field'})
    submit = SubmitField(label='Submit',render_kw={'class': 'submit-design'})

    def validate_email(self, email):
        """this method will check if the email is already used by another user"""
        email = User.query.filter_by(email=email.data).first()

        if email:
            raise ValidationError(f'email already exists try another one')

    def validate_username(self, username):
        """this method will check if username is already taken"""
        username = User.query.filter_by(username=username.data).first()
        if username:
            raise ValidationError(f'username is taken try another one')

        

class LoginPatient(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email()], render_kw={'class': 'design-field'})
    password = PasswordField(label='Password', validators=[DataRequired()], render_kw={'class': 'design-field'})
    submit = SubmitField(label='Login', render_kw={'class': 'submit-design'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5030, debug=True)
