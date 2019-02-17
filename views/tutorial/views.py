from pyramid.response import Response
from pyramid.view import view_config

# /
@view_config(route_name='home')
def home(request):
    return Response('<body>Go to <a href="/hello">hello</a></body>')

# /hello
@view_config(route_name='hello')
def hello(request):
    return Response('<body>Go to <a href="/">home</a></body>')
