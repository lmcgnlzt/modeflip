from pyramid.httpexceptions import exception_response
from modeflip.models.designer import Designer, DesignerConfig
from modeflip.models.collection import Collection, CollectionConfig
from modeflip.models.garment import Garment, GarmentConfig


class ModeAPI(object):

	def __init__(self, context, request):
		self.request = request
		config_db = request.get_database('mf_config')
		self.dc = DesignerConfig(config_db)
		self.cc = CollectionConfig(config_db)
		self.gc = GarmentConfig(config_db)

	# GET /modeapi/portfolios/{did:\d+}
	def get_portfolio_by_did(self):
		did = int(self.request.matchdict['did'])
		ret = self.dc.get(did)
		if ret:
			collection_data = []
			collections = self.cc.get_latest_collections_by_designer(did, limit=2)
			for collection in collections:
				garments = self.gc.get_all_garments_by_designer_collection(did, collection.cid)
				collection.garments = garments
				collection_data.append(collection)
			ret.collections = collection_data
			return ret

	# GET /modeapi/portfolios/{curr_did:\d+}/next
	def get_next_portfolio(self):
		curr_did = int(self.request.matchdict['curr_did'])
		designer, has_next = self.dc.get_next_designer(curr_did)
		if designer:
			did = designer.did
			collection_data = []
			collections = self.cc.get_latest_collections_by_designer(did, limit=2)
			for collection in collections:
				garments = self.gc.get_all_garments_by_designer_collection(did, collection.cid)
				collection.garments = garments
				collection_data.append(collection)
			designer.collections = collection_data
			return {'did': designer.did, 'designer': designer, 'has_next': has_next}
		else:
			return {}

	# GET /modeapi/garments/{did:\d+}/{cid:\d+}/{gid:\d+}
	def get_garment_info(self):
		did = int(self.request.matchdict['did'])
		cid = int(self.request.matchdict['cid'])
		gid = int(self.request.matchdict['gid'])
		return self.gc.get(did, cid, gid)

	# GET /modeapi/experience/{did:\d+}
	def get_experience_info(self):
		did = int(self.request.matchdict['did'])
		return self.dc.get(did).experience_content.pics

	# GET /modeapi/dids
	def get_dids(self):
		return self.dc.get_all_ids()

	# GET /modeapi/designers
	def get_designers(self):
		ret = self.dc.get_all_designers()
		return ret

	# GET /modeapi/designers/{did:\d+}
	def get_designer(self):
		did = int(self.request.matchdict['did'])
		return self.dc.get(did)



def add_view(config, route_name, method, attr):
	handler = 'modeflip.api_internal.mode_api:ModeAPI'
	config.add_view(
		handler,
		attr=attr,
		route_name=route_name,
		request_method=method,
		renderer='json'
		)


def includeme(config):

	config.add_route('portfolio_by_did', '/modeapi/portfolios/{did:\d+}')
	add_view(config, 'portfolio_by_did', 'GET', 'get_portfolio_by_did')

	config.add_route('next_portfolio', '/modeapi/portfolios/{curr_did:\d+}/next')
	add_view(config, 'next_portfolio', 'GET', 'get_next_portfolio')

	config.add_route('garment_info', '/modeapi/garments/{did:\d+}/{cid:\d+}/{gid:\d+}')
	add_view(config, 'garment_info', 'GET', 'get_garment_info')

	config.add_route('experience_info', '/modeapi/experience/{did:\d+}')
	add_view(config, 'experience_info', 'GET', 'get_experience_info')

	config.add_route('did_list', '/modeapi/dids')
	add_view(config, 'did_list', 'GET', 'get_dids')

	config.add_route('designer_list', '/modeapi/designers')
	add_view(config, 'designer_list', 'GET', 'get_designers')

	config.add_route('designer', '/modeapi/designers/{did:\d+}')
	add_view(config, 'designer', 'GET', 'get_designer')