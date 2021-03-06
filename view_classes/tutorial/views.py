from pyramid.response import Response
from pyramid.view import (
    view_config,
    view_defaults
)

@view_defaults(renderer='home.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    # /
    @view_config(route_name='home')
    def home(request):
        return {'name': 'home'}

    # /hello
    @view_config(route_name='hello')
    def hello(request):
        return {'name': 'hello'}
