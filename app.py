from flask import Flask, render_template, session

from flask.ext.restful import Api

app = Flask(__name__)
app.config.from_object('config.settings.DevelpmentConfig')


with app.app_context():
	from models import *
	import apis

@app.route('/')
def index():
	user_id = session.get('user_id', 1)

	cats = Category.query.filter('user_id=:user_id').params(user_id=user_id).all()	
	results = []
	for c in cats:
		webs = WebSite.query.filter('category_id=:category_id').params(category_id=c.id).all()
		results.append({c: webs})

	step = 5
	navis = [[]] * step
	for n, r in enumerate(results):
		navis[n % step].append(r)

	return render_template('index.html', navis=navis)

def main():
	app.run(debug=True)

if __name__ == '__main__':
	main()
