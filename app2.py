from flask import Flask, render_template, request
from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectMultipleField
from wtforms.validators import DataRequired

AVAILABLE_CHOICES = [('dog', 'Dogs'), ('cat', 'Cats'), ('liz', 'Lizard')]

class Selection(FlaskForm):
	selection = SelectMultipleField(choices=AVAILABLE_CHOICES)

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/reggie2', methods=['GET','POST'])
def reply():
	if request.method == 'POST':
		formList = request.form.getlist('tests')
	return ', '.join(str(x) for x in formList)

@app.route("/login", methods=['GET','POST'])
def login():
	return render_template('login.html', title="Sign In")

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)