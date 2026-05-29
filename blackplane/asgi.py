"""ASGI config for blackplane project."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blackplane.settings")

application = get_asgi_application()
