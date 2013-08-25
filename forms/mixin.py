class FormMixin(object):
	def fill_data_to_instance(self, instance):
		for k, v in self._fields.items():
			setattr(instance, k, v.data)

		return instance
