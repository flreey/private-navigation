from flask import jsonify, request, session

from flask.ext.restful import Resource

from app import api
from libs.util import login_required
from models.user import User
from forms.user_form import ApiUserForm


class ApiUser(Resource):
	@login_required
	def get(self, user_id):
		return jsonify(User.get(user_id).json)

	def post(self):
		form = ApiUserForm(request.form)
		if form.validate():
			u = User(name=form.name.data,
					password=form.password.data,
					email=form.email.data).insert()
			return jsonify(code=0, data=u.json)
		return jsonify({'code': 1, 'message': form.errors})

	@login_required
	def put(self):
		form = ApiUserForm(request.form)
		if form.validate():
			u = User.get(session['user_id'])
			u.name = form.name.data
			u.email = form.email.data
			u.password = form.password.data
			u.update()
			return jsonify(code=0, data=u.json)
		return jsonify({'code': 1, 'message': form.errors})

	@login_required
	def delete(self, user_id):
		u = User.get(user_id)
		if u:
			u.delete()
			return jsonify({'code': 0})
		return jsonify({'code': 1, 'message': 'user not exist'})

api.add_resource(ApiUser, '/api/user', '/api/user/<int:user_id>')
