from wtforms import TextField, Form
from wtforms.validators import Required, Optional

from .mixin import FormMixin

class ApiWebSiteForm(Form, FormMixin):
	title = TextField('title', validators=[Required()])
	url = TextField('url', validators=[Required()])
	category_id = TextField('category_id', validators=[Optional()])
	descr = TextField('descr', validators=[Optional()])
	image = TextField('image', validators=[Optional()])
