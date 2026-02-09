"""
WSGI config for fullstackcrud project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

"""
WSGI config for fullstackcrud project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys

# IMPORTANT: add your project directory to Python path
path = '/home/resiliencesoft/python_project'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fullstackcrud.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

