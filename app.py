from flask import Flask, render_template, session, request, redirect

from forms.user_form import UserForm

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

@app.route('/')
def index():
	user_id = session.get('user_id', 1)

	cats = Category.query.filter_by(user_id=user_id).order_by('title').all()	
	results = []
	for c in cats:
		webs = WebSite.query.filter('category_id=:category_id').params(category_id=c.id).all()
		results.append({c: webs})

	step = min(len(results), 5)
	navis = [[] for i in range(step)]
	for n, r in enumerate(results):
		navis[n % step].append(r)

	user = User.get(session.get('user_id'))
	user = user.json if user else None
	return render_template('index.html', navis=navis, user=user, form=UserForm())


@app.route('/login', methods=['POST'])
def login():
	form = UserForm(request.form)
	if form.validate():
		email = form.email.data
		u = User.query.filter_by(email=email).first()
		if u and u.valid_password(form.password.data):
			session['user_id'] = u.id
	return redirect('/')

@app.route('/logout', methods=['GET'])
def logout():
	del session['user_id']
	return redirect('')

def main():
	app.run(debug=True)

if __name__ == '__main__':
	main()
