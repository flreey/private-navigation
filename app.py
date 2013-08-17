from flask import Flask, render_template, session

app = Flask(__name__)
app.config.from_object('config.settings.DevelpmentConfig')

with app.app_context():
	from models.website import WebSite

@app.route('/')
def index():
	if not session.get('user_id'):
		websites = WebSite.query.all()
		print(websites)
		return render_template('index.html')

def main():
	app.run(debug=True)

if __name__ == '__main__':
	main()
