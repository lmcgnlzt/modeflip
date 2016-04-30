from pyramid.httpexceptions import exception_response
from modeflip.models.designer import Designer, DesignerConfig
from modeflip.models.collection import Collection, CollectionConfig
from modeflip.models.garment import Garment, GarmentConfig


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

	# GET /designers_by_page?_page=1&_perPage=10
	def get_designers_by_page(self):
		_page = int(self.request.params['_page'])
		_perPage = int(self.request.params['_perPage'])
		return self.dc.get_designers_by_page(_page, _perPage)

	# GET /designers/{did}
	def get_designer_by_id(self):
		did = int(self.request.matchdict['did'])
		designer = self.dc.get(did)
		if not designer:
			raise exception_response(400, body='Designer does not exist')
		return designer

	# POST /designers
	def create_designer(self):
		data = self.request.json_body
		if 'did' not in data:
			raise exception_response(400, body='Invalid designer data')
		did = int(str(data['did']))
		if self.dc.get(did):
			raise exception_response(400, body='Designer already exists')
		try:
			self.dc.set(Designer(**data))
		except Exception as e:
			raise exception_response(500, body=str(e))
		self.request.response.status_int = 201
		return data

	# PUT /designers/{did}
	def update_designer_by_id(self):
		did = int(self.request.matchdict['did'])
		data = self.request.json_body
		designer = Designer(**data)
		if did != designer.did:
			raise exception_response(400, body='Designer ID does not match')
		try:
			self.dc.set(designer)
		except Exception as e:
			raise exception_response(500, body=str(e))
		return data

	# DELETE /designers/{did}
	def delete_designer_by_id(self):
		did = int(self.request.matchdict['did'])
		deleted = self.dc.delete(did)
		if deleted:
			return {'success': True}
		else:
			raise exception_response(400, body='Designer does not exist')

	# GET /designers/{did:\d+}/likes
	def get_likes_by_did(self):
		did = int(self.request.matchdict['did'])
		return self.dc.get_likes(did)

	# PUT /designers/{did:\d+}/do_like
	def like_designer(self):
		did = int(self.request.matchdict['did'])
		return self.dc.do_like(did)

	# GET /designers/{did:\d+}/subscribes
	def get_subscribes_by_did(self):
		did = int(self.request.matchdict['did'])
		return self.dc.get_subscribes(did)

	# PUT /designers/{did:\d+}/do_subscribe
	def subscribe_designer(self):
		did = int(self.request.matchdict['did'])
		return self.dc.do_subscribe(did)

	# GET /designers/{did:\d+}/collections
	def get_collections_by_designer(self):
		did = int(self.request.matchdict['did'])
		return self.cc.get_all_collections_by_designer(did)

	# GET /designers/{did:\d+}/collections/{cid:\d+}
	def get_collection_by_id(self):
		did = int(self.request.matchdict['did'])
		cid = int(self.request.matchdict['cid'])
		return self.cc.get(did, cid)

	# POST /designers/{did:\d+}/collections
	def create_collection(self):
		data = self.request.json_body
		from pprint import pprint
		pprint(data)
		if 'did' not in data or 'cid' not in data:
			raise exception_response(400, body='Invalid collection data')
		did = int(str(data['did']))
		cid = int(str(data['cid']))
		if self.cc.get(did, cid):
			raise exception_response(400, body='Collection already exists')
		try:
			self.cc.set(Collection(**data))
		except Exception as e:
			raise exception_response(500, body=str(e))
		self.request.response.status_int = 201
		return data

	# PUT /designers/{did}/collections/{cid:\d+}
	def update_collection_by_id(self):
		did = int(self.request.matchdict['did'])
		cid = int(self.request.matchdict['cid'])
		data = self.request.json_body
		collection = Collection(**data)
		if did != collection.did or cid != collection.cid:
			raise exception_response(400, body='Designer and collection IDs do not match')
		try:
			self.cc.set(collection)
		except Exception as e:
			raise exception_response(500, body=str(e))
		return data

	# DELETE /designers/{did}/collections/{cid:\d+}
	def delete_collection_by_id(self):
		did = int(self.request.matchdict['did'])
		cid = int(self.request.matchdict['cid'])
		deleted = self.cc.delete(did, cid)
		if deleted:
			return {'success': True}
		else:
			raise exception_response(400, body='Collection does not exist')

	# GET /designers/{did:\d+}/collections/{cid:\d+}/garments
	def get_garments_by_designer_collection(self):
		did = int(self.request.matchdict['did'])
		cid = int(self.request.matchdict['cid'])
		return self.gc.get_all_garments_by_designer_collection(did, cid)

	# POST /designers/{did:\d+}/collections/{cid:\d+}/garments
	def create_garment(self):
		data = self.request.json_body
		if 'did' not in data or 'cid' not in data or 'gid' not in data:
			raise exception_response(400, body='Invalid garment data')
		did = int(str(data['did']))
		cid = int(str(data['cid']))
		gid = int(str(data['gid']))
		if self.gc.get(did, cid, gid):
			raise exception_response(400, body='Garment already exists')
		try:
			self.gc.set(Garment(**data))
		except Exception as e:
			raise exception_response(500, body=str(e))
		self.request.response.status_int = 201
		return data

	# GET /designers/{did:\d+}/collections/{cid:\d+}/garments/{gid:\d+}
	def get_garment_by_id(self):
		did = int(self.request.matchdict['did'])
		cid = int(self.request.matchdict['cid'])
		gid = int(self.request.matchdict['gid'])
		return self.gc.get(did, cid, gid)

	# PUT /designers/{did:\d+}/collections/{cid:\d+}/garments/{gid:\d+}
	def update_garment_by_id(self):
		did = int(self.request.matchdict['did'])
		cid = int(self.request.matchdict['cid'])
		gid = int(self.request.matchdict['gid'])
		data = self.request.json_body
		garment = Garment(**data)
		if did != garment.did or cid != garment.cid or gid != garment.gid:
			raise exception_response(400, body='Designer and collection and garment IDs do not match')
		try:
			self.gc.set(garment)
		except Exception as e:
			raise exception_response(500, body=str(e))
		return data

	# DELETE /designers/{did:\d+}/collections/{cid:\d+}/garments/{gid:\d+}
	def delete_garment_by_id(self):
		did = int(self.request.matchdict['did'])
		cid = int(self.request.matchdict['cid'])
		gid = int(self.request.matchdict['gid'])
		deleted = self.gc.delete(did, cid, gid)
		if deleted:
			return {'success': True}
		else:
			raise exception_response(400, body='Garment does not exist')


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
	add_view(config, 'designers', 'POST', 'create_designer')

	config.add_route('designers_by_page', '/designers_by_page')
	add_view(config, 'designers_by_page', 'GET', 'get_designers_by_page')

	config.add_route('designer_by_did', '/designers/{did:\d+}')
	add_view(config, 'designer_by_did', 'GET', 'get_designer_by_id')
	add_view(config, 'designer_by_did', 'PUT', 'update_designer_by_id')
	add_view(config, 'designer_by_did', 'DELETE', 'delete_designer_by_id')

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
	add_view(config, 'collections_by_designer', 'POST', 'create_collection')

	config.add_route('collection_by_id', '/designers/{did:\d+}/collections/{cid:\d+}')
	add_view(config, 'collection_by_id', 'GET', 'get_collection_by_id')
	add_view(config, 'collection_by_id', 'PUT', 'update_collection_by_id')
	add_view(config, 'collection_by_id', 'DELETE', 'delete_collection_by_id')


	config.add_route('garments_by_designer_collection', '/designers/{did:\d+}/collections/{cid:\d+}/garments')
	add_view(config, 'garments_by_designer_collection', 'GET', 'get_garments_by_designer_collection')
	add_view(config, 'garments_by_designer_collection', 'POST', 'create_garment')

	config.add_route('garment_by_id', '/designers/{did:\d+}/collections/{cid:\d+}/garments/{gid:\d+}')
	add_view(config, 'garment_by_id', 'GET', 'get_garment_by_id')
	add_view(config, 'garment_by_id', 'PUT', 'update_garment_by_id')
	add_view(config, 'garment_by_id', 'DELETE', 'delete_garment_by_id')


