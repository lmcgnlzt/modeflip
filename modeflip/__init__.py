from pyramid.config import Configurator
from modeflip.utils.config import get_configuration
from modeflip.utils.mongo import MongoManager
from modeflip.utils import pyramid_helpers


def setup_storage(config):
	global get_database
	config.registry['configuration'] = get_configuration()
	local_config = config.registry['configuration']
	get_database = MongoManager(local_config, force_load=True)
	config.registry['get_database'] = get_database


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    # config.add_static_view('static', 'static', cache_max_age=3600)
    # config.add_route('home', '/')

    setup_storage(config)
    config.include('modeflip.utils.pyramid_helpers')


    # config.include('modeflip.api_internal.frontpage_api')
    config.include('modeflip.api_internal.designer_api')


    # config.scan()
    return config.make_wsgi_app()
