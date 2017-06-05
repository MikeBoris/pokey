from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectMultipleField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
   user_id = StringField('user_id', validators=[DataRequired()])
   remember_me = BooleanField('remember_me', default=False)

class Selection(FlaskForm):
	selection = SelectMultipleField('selector', choices=[('dog', 'Dogs'), ('cat', 'Cats'), ('liz', 'Lizard')])
