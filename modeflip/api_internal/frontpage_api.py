from pyramid.httpexceptions import exception_response


class FrontpageAPI(object):

	def __init__(self, context, request):
		self.context = context
		self.request = request


def add_view(config, route_name, method, attr):
	handler = 'modeflip.api_internal.frontpage_api:FrontpageAPI'
	config.add_view(
		handler,
		attr=attr,
		route_name=route_name,
		request_method=method,
		renderer='json'
		)


def includeme(config):
	pass