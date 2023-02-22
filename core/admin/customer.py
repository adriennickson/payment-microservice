"""Customer Admin"""
from django.contrib import admin

from core.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Customer Admin"""

    list_display = ("email", "platform")
    search_fields = ("email", "platform")
    list_filter = ("platform",)
