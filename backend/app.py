from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='../frontend/templates')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """This brings a user to the home page of the app"""
    return render_template('home.html', title='Home')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5030, debug=True)
