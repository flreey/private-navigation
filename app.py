from flask import Flask, render_template, session, jsonify, request
from flask.ext.restful import Resource, Api

from forms.user_form import ApiUserForm

app = Flask(__name__)
app.config.from_object('config.settings.DevelpmentConfig')

api = Api(app)

with app.app_context():
	from models import *

@app.route('/')
def index():
	user_id = session.get('user_id', 1)

	cats = Category.query.filter('user_id=:user_id').params(user_id=user_id).all()	
	results = []
	for c in cats:
		webs = WebSite.query.filter('category_id=:category_id').params(category_id=c.id).all()
		results.append({c: webs})

	step = 5
	navis = [[] for i in range(step)]
	for n, r in enumerate(results):
		navis[n % step].append(r)

	return render_template('index.html', navis=navis)

class ApiUser(Resource):
	def get(self, user_id):
		return jsonify(User.get(user_id).json)

	def post(self):
		form = ApiUserForm(request.form)
		if form.validate():
			password = request.form['password']
			email = request.form['email']
			name = request.form['name']
			u = User(name=name, password=password, email=email).insert()
			return jsonify(u.json)
		return jsonify({'code': 1, 'message': form.errors})

	def put(self):
		pass

	def delete(self):
		pass

api.add_resource(ApiUser, '/api/user', '/api/user/<int:user_id>')

def main():
	app.run(debug=True)

if __name__ == '__main__':
	main()
