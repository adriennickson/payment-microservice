# flake8: noqa
from .base import *  # pylint: disable=W0401,W0614

MIDDLEWARE = MIDDLEWARE + ["corsheaders.middleware.CorsMiddleware"]
INSTALLED_APPS = INSTALLED_APPS + ["corsheaders"]
ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True
