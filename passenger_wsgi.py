import os
import sys


# sys.path.insert(0, os.path.dirname(__file__))

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))


# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     message = 'It works! svdvd asdv\n'
#     version = 'Python %s\n' % sys.version.split()[0]
#     response = '\n'.join([message, version])
#     return [response.encode()]


from gmk_api.wsgi import application