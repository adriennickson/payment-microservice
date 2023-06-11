# flake8: noqa
from .base import *  # pylint: disable=wildcard-import, unused-wildcard-import, relative-beyond-top-level, useless-suppression

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
}
