from flask_wtf import Form as sForm
from wtforms import TextField, Form
from wtforms.validators import Required, EqualTo
from sqlalchemy import or_

from .mixin import FormMixin

class ApiUserForm(Form, FormMixin):
	email = TextField('email', validators=[Required()])
	name = TextField('name', validators=[Required()])
	password = TextField('password', validators=[Required()])

class UserForm(sForm, FormMixin):
	email = TextField('email', validators=[Required()])
	password = TextField('password', validators=[Required()])

class RegisterForm(UserForm):
	name = TextField('name', validators=[Required()])
	email = TextField('email', validators=[Required()])
	password = TextField('password', validators=[Required()])
	confirm = TextField('confirm', validators=[Required(), EqualTo('password')])

	def validate(self):
		from models.user import User

		if super().validate():
			u = User.query.filter(or_(User.name==self.name.data, User.email==self.email.data)).first()
			if u:
				if u.name == self.name.data:
					self.name.errors.append('user name exists')
				elif u.email == self.email.data:
					self.email.errors.append('email exists')
				return False
			return True
		return False
