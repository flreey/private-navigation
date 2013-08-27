from flask_wtf import Form as sForm
from wtforms import TextField, Form
from wtforms.validators import Required

from .mixin import FormMixin

class ApiUserForm(Form, FormMixin):
	email = TextField('email', validators=[Required()])
	name = TextField('name', validators=[Required()])
	password = TextField('password', validators=[Required()])

class UserForm(sForm, FormMixin):
	email = TextField('email', validators=[Required()])
	password = TextField('password', validators=[Required()])
