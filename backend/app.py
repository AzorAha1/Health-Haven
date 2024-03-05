from flask import Flask, render_template, url_for,redirect, flash
from auth import RegisterPatient, LoginPatient
app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/styles')
app.config['SECRET_KEY'] = 'd408adac2785c9429f66f099f0d2a4a4'

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
        flash(message=f'Account Created for {form.username.data}', category='success')
        print(form.username.data)
        return redirect(url_for('home'))
    print(form.data)
    print(form.errors) # Temporary debug line
    return render_template('register.html', title='Login', form=form)
@app.route('/about')
def about():
    """This brings a user to the about page of the app"""
    return render_template('about.html', title='Home')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5030, debug=True)
