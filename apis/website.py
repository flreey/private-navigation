from flask import jsonify, request, session

from flask.ext.restful import Resource

from app import api
from libs.util import login_required
from models.website import WebSite
from forms.website_form import ApiWebSiteForm


class ApiWebSite(Resource):
	@login_required
	def get(self, site_id):
		return jsonify({'code': 0, 'data': WebSite.get(site_id).json})

	@login_required
	def post(self):
		form = ApiWebSiteForm(request.form)
		if form.validate():
			w = form.fill_data_to_instance(WebSite())
			w.insert()
			return jsonify(code=0, data=w.json)
		return jsonify({'code': 1, 'message': form.errors})

	@login_required
	def put(self, site_id):
		form = ApiWebSiteForm(request.form)
		if form.validate():
			w = form.fill_data_to_instance(WebSite.get(site_id))
			w.update()
			return jsonify(code=0, data=w.json)
		return jsonify({'code': 1, 'message': form.errors})

	@login_required
	def delete(self, site_id):
		u = WebSite.get(site_id)
		if u:
			u.delete()
			return jsonify({'code': 0})
		return jsonify({'code': 1, 'message': 'website not exist'})

api.add_resource(ApiWebSite, '/api/website',
'/api/website/<int:site_id>')
