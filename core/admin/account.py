"""OrderA Admin"""
from django.contrib import admin

from core.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Account Admin"""
