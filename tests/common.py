import json

import app as pn

class JSON:
	def _recurse_dumps(self, dct):
		d = {}
		for k, v in dct.items():
			if isinstance(v, JSON):
				v = self._recurse_dumps(v.__dict__)
			d[k] = v

		return json.dumps(d)

	def __str__(self):
		return self._recurse_dumps(self.__dict__)

class Common:
	def __init__(self):
		pn.app.config['TESTING'] = True
		self.app = pn.app.test_client()

	def setup(self):
		pass

	def teardown(self):
		pass

	def get(self, uri):
		self.r = self.app.get(uri)
		return self.r

	def post(self, uri, data=None):
		self.r = self.app.post(uri, data=data)
		return self.r

	def put(self, uri, data=None):
		self.r = self.app.put(uri, data=data)
		return self.r

	def delete(self, uri):
		self.r = self.app.delete(uri)
		return self.r

	def _object_hook(self, dct):
		d = JSON()
		for k , v in dct.items():
			if isinstance(v, dict):
				v = self._object_hook(v)
			setattr(d, k, v)

		return d

	def jsonify_response_data(self):
		return json.loads(self.r.data.decode('utf8'), object_hook=self._object_hook)
