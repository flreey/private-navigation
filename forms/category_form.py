from wtforms import TextField, IntegerField, Form
from wtforms.validators import Required
from .custom_validators import NumberOptional

from .mixin import FormMixin

class ApiCategoryForm(Form, FormMixin):
	parent = IntegerField('parent', validators=[NumberOptional()], default=0)
	title = TextField('title', validators=[Required()])
	descr = TextField('descr', validators=[Required()])
