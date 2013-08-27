import sys
sys.path.insert(0, '../')

from app import app

with app.app_context():
	from models.base import init_db, Base, engine
	from models import *


	Base.metadata.drop_all(bind=engine)
	init_db()

	u = User(name='flreey', email='flreey@gmail.com', password='123456').insert()

	data = {'Blog': ['InfoQ', 'ItEye', 'CSDN', 'Solidot', '技术博客'],
	'Design': ['Mile', '淘宝UED' * 2, '腾讯UX'], 'Launguage': ['Python', 'Java',
		'Erlang', 'Haskel', 'Jquery', 'Css'], 'Tools': ['Vim', 'HHKB',
			'Mockup', 'LiveReload' * 2], 'Apple' * 2: ['IOS',
				'IPHONE', 'IPad', 'MacOS']}

	for i in range(3):
		for k, v in data.copy().items():
			data[k+'1'] = v

	for cat, websites in data.items():
		c = Category(user_id=u.id, title=cat).insert()
		[WebSite(title=w, url='#', category_id=c.id).insert() for w in websites]
