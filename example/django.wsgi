import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
os.environ['DJANGO_SETTINGS_MODULE'] = 'example.settings'

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()


