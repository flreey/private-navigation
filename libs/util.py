from functools import wraps
from flask import session, request

from .exception import AuthorticationException

def login_required(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		user_id = request.cookies.get('user_id') or session.get('user_id')
		if user_id:
			session['user_id'] = user_id
			return func(*args, **kwargs)
		raise AuthorticationException('user not login')

	return wrapper

def user_login(user):
	session['user_id'] = user.id
