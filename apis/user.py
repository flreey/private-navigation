from flask import jsonify, request, session, current_app

from flask.ext.restful import Resource, Api

from libs.util import login_required
from models.user import User
from forms.user_form import ApiUserForm

api = Api(current_app)

class ApiUser(Resource):
	@login_required
	def get(self, user_id):
		return jsonify({'code': 0, 'data': User.get(user_id).json})

	def post(self):
		form = ApiUserForm(request.form)
		if form.validate():
			u = form.fill_data_to_instance(User())
			u.insert()
			return jsonify(code=0, data=u.json)
		return jsonify({'code': 1, 'message': form.errors})

	@login_required
	def put(self):
		form = ApiUserForm(request.form)
		if form.validate():
			u = User.get(session['user_id'])
			form.fill_data_to_instance(u)
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

@current_app.route('/api/login', methods=['post'])
def login():
	email = request.form['email']
	password = request.form['password']
	u = User.query.filter_by(email=email).first()
	if u and u.valid_password(password):
		session['user_id'] = u.id
		res = jsonify({'code': 0, 'data': u.json})
		res.set_cookie('user_id', str(u.id))
		return res
	return jsonify({'code': 1, 'message': 'email or password not correct'})
