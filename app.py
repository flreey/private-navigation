from flask import Flask, render_template, session, request, redirect

from forms.user_form import UserForm, RegisterForm
from libs.util import user_login

app = Flask(__name__)

import os
if os.environ.get('PN', 'DEV') == 'DEV':
	config_object = 'config.settings.DevelopmentConfig'
else:
	config_object = 'config.settings.ProductionConfig'

app.config.from_object(config_object)

with app.app_context():
	from models import *
	import apis

@app.route('/', methods=['GET', 'POST'])
def index():
	form = UserForm(request.form)
	if request.method == 'POST':
		if form.validate():
			email = form.email.data
			u = User.query.filter_by(email=email).first()
			if not u:
				form.email.errors.append('Eamil is incorrect')
			elif not u.valid_password(form.password.data):
				form.password.errors.append('Password is incorrect')
			else:
				user_login(u)

	user = User.get(session.get('user_id'))
	user_id = user.id if user else 1

	cats = Category.query.filter_by(user_id=user_id).order_by('title').all()	
	results = []
	for c in cats:
		webs = WebSite.query.filter('category_id=:category_id').params(category_id=c.id).all()
		results.append({c: webs})

	step = min(len(results), 5)
	navis = [[] for i in range(step)]
	for n, r in enumerate(results):
		navis[n % step].append(r)

	return render_template('index.html', navis=navis, user=user, form=form)

@app.route('/login', methods=['POST'])
def login():
		return redirect('/')

@app.route('/logout', methods=['GET'])
def logout():
	del session['user_id']
	return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if request.method == 'POST' and form.validate():
		u = form.fill_data_to_instance(User())
		u.insert()
		user_login(u)
		return redirect('/')

	return render_template('register.html', form=form)

def main():
	app.run(debug=True)

if __name__ == '__main__':
	main()
