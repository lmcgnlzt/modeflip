from pyramid.view import view_config
from modeflip.models.designer import Designer


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'modeflip'}


if __name__ == '__main__':
	print Designer()