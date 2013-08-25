from wtforms import ValidationError
from wtforms.validators import Optional

class NumberOptional(Optional):
	def __call__(self, form, field):
		super().__call__(form, field)
		data = field.data
		if not data or not isinstance(data, int):
			raise ValidationError('data must be integer')
