from wtforms import TextField, Form
from wtforms.validators import Required

class ApiUserForm(Form):
	email = TextField('email', validators=[Required()])
	name = TextField('name', validators=[Required()])
	password = TextField('password', validators=[Required()])
