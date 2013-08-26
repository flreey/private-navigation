from flask import jsonify, request, session, current_app

from flask.ext.restful import Resource, Api

from libs.util import login_required
from models.category import Category
from forms.category_form import ApiCategoryForm

api = Api(current_app)

class ApiCategory(Resource):
	@login_required
	def get(self, cat_id):
		return jsonify({'code': 0, 'data':Category.get(cat_id).json})

	@login_required
	def post(self):
		form = ApiCategoryForm(request.form)
		if form.validate():
			c = form.fill_data_to_instance(Category())
			c.user_id = session['user_id']
			c.insert()
			return jsonify(code=0, data=c.json)
		return jsonify({'code': 1, 'message': form.errors})

	@login_required
	def put(self, cat_id):
		form = ApiCategoryForm(request.form)
		if form.validate():
			c = Category.get(cat_id)
			if c.user_id != session['user_id']:
				return jsonify({'code': 2, 'message': 'has no permission to modify the category'})
			else:
				form.fill_data_to_instance(c)
				return jsonify(code=0, data=c.json)
		return jsonify({'code': 1, 'message': form.errors})

	@login_required
	def delete(self, cat_id):
		c = Category.get(cat_id)
		if c:
			c.delete()
			return jsonify({'code': 0})
		return jsonify({'code': 1, 'message': 'category not exist'})

api.add_resource(ApiCategory, '/api/category', '/api/category/<int:cat_id>')
