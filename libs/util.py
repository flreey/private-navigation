from functools import wraps
from flask import session

from .exception import AuthorticationException

def login_required(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		if session.get('user_id'):
			return func(*args, **kwargs)
		raise AuthorticationException('user not login')

	return wrapper
