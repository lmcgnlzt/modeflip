from pyramid.httpexceptions import exception_response
from modeflip.models.designer import DesignerConfig
from modeflip.models.collection import CollectionConfig
from modeflip.models.garment import GarmentConfig


class DesignerAPI(object):

	def __init__(self, context, request):
		self.context = context
		self.request = request
		self.dc = DesignerConfig(request.get_database('mf_config'))
		self.cc = CollectionConfig(request.get_database('mf_config'))
		self.gc = GarmentConfig(request.get_database('mf_config'))

	# GET /designers
	def get_all_designers(self):
		return self.dc.get_all_designers()

	# GET /designers/{did}
	def get_by_did(self):
		did = int(self.request.matchdict.get('did'))
		designer = self.dc.get(did)
		if not designer:
			raise exception_response(400, body='designer does not exist')
		return designer

	# GET /designers/{did:\d+}/likes
	def get_likes_by_did(self):
		did = int(self.request.matchdict.get('did'))
		return self.dc.get_likes(did)

	# PUT /designers/{did:\d+}/do_like
	def like_designer(self):
		did = int(self.request.matchdict.get('did'))
		return self.dc.do_like(did)

	# GET /designers/{did:\d+}/subscribes
	def get_subscribes_by_did(self):
		did = int(self.request.matchdict.get('did'))
		return self.dc.get_subscribes(did)

	# PUT /designers/{did:\d+}/do_subscribe
	def subscribe_designer(self):
		did = int(self.request.matchdict.get('did'))
		return self.dc.do_subscribe(did)

	# GET /designers/{did:\d+}/collections
	def get_collections_by_designer(self):
		did = int(self.request.matchdict.get('did'))
		return self.cc.get_all_collections_by_designer(did)

	# GET /designers/{did:\d+}/collections/{cid:\d+}
	def get_collection_by_id(self):
		did = int(self.request.matchdict.get('did'))
		cid = int(self.request.matchdict.get('cid'))
		return self.cc.get(did, cid)

	# GET /designers/{did:\d+}/collections/{cid:\d+}/garments
	def get_garments_by_designer_collection(self):
		did = int(self.request.matchdict.get('did'))
		cid = int(self.request.matchdict.get('cid'))
		return self.gc.get_all_garments_by_designer_collection(did, cid)

	# GET /designers/{did:\d+}/collections/{cid:\d+}/garments/{oid:\d+}
	def get_garment_by_id(self):
		did = int(self.request.matchdict.get('did'))
		cid = int(self.request.matchdict.get('cid'))
		oid = int(self.request.matchdict.get('oid'))
		return self.gc.get(did, cid, oid)



def add_view(config, route_name, method, attr):
	handler = 'modeflip.api_internal.designer_api:DesignerAPI'
	config.add_view(
		handler,
		attr=attr,
		route_name=route_name,
		request_method=method,
		renderer='json'
		)


def includeme(config):
	config.add_route('designers', '/designers')
	add_view(config, 'designers', 'GET', 'get_all_designers')

	config.add_route('designer_by_did', '/designers/{did:\d+}')
	add_view(config, 'designer_by_did', 'GET', 'get_by_did')

	config.add_route('likes_of_designer', '/designers/{did:\d+}/likes')
	add_view(config, 'likes_of_designer', 'GET', 'get_likes_by_did')

	config.add_route('like_designer', '/designers/{did:\d+}/do_like')
	add_view(config, 'like_designer', 'PUT', 'like_designer')

	config.add_route('subscribes_of_designer', '/designers/{did:\d+}/subscribes')
	add_view(config, 'subscribes_of_designer', 'GET', 'get_subscribes_by_did')

	config.add_route('subscribe_designer', '/designers/{did:\d+}/do_subscribe')
	add_view(config, 'subscribe_designer', 'PUT', 'subscribe_designer')

	config.add_route('collections_by_designer', '/designers/{did:\d+}/collections')
	add_view(config, 'collections_by_designer', 'GET', 'get_collections_by_designer')

	config.add_route('collection_by_id', '/designers/{did:\d+}/collections/{cid:\d+}')
	add_view(config, 'collection_by_id', 'GET', 'get_collection_by_id')

	config.add_route('garments_by_designer_collection', '/designers/{did:\d+}/collections/{cid:\d+}/garments')
	add_view(config, 'garments_by_designer_collection', 'GET', 'get_garments_by_designer_collection')

	config.add_route('garment_by_id', '/designers/{did:\d+}/collections/{cid:\d+}/garments/{oid:\d+}')
	add_view(config, 'garment_by_id', 'GET', 'get_garment_by_id')


