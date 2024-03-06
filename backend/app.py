from flask import Flask, render_template, url_for,redirect, flash, request
from auth import RegisterPatient, LoginPatient
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from datetime import datetime

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/styles')
app.config['SECRET_KEY'] = 'd408adac2785c9429f66f099f0d2a4a4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/health-haven.db'


db = SQLAlchemy(app=app)
bcrypt = Bcrypt(app=app)
migrate = Migrate(app, db)



class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True, nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    phonenum = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f'the user id is {self.user_id}, the email is {self.email}, the username is {self.username}'

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
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.doctor_id'))

    user = db.relationship('User', backref=db.backref('appointments', lazy=True))
    doctor = db.relationship('Doctor', backref=db.backref('appointments', lazy=True))


    
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """This brings a user to the home page of the app"""
    return render_template('home.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """This brings a user to the login page of the app"""
    form = LoginPatient()
    return render_template('login.html', title='Login', form=form)

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5030, debug=True)
