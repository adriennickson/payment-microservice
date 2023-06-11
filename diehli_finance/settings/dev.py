# flake8: noqa
from .base import *  # pylint: disable=wildcard-import, unused-wildcard-import, relative-beyond-top-level, useless-suppression

MIDDLEWARE = MIDDLEWARE + [  # pylint: disable=E0601
    "corsheaders.middleware.CorsMiddleware"
]
INSTALLED_APPS = INSTALLED_APPS + ["corsheaders"]  # pylint: disable=E0601
ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True
