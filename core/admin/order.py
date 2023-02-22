"""OrderA Admin"""
from django.contrib import admin

from core.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """OrderA Admin"""

    list_display = ("pk", "get_email", "get_platform")
    search_fields = ("get_email", "get_platform")
    # list_filter = ('get_platform',)

    @admin.display(ordering="customer__email", description="email")
    def get_email(self, obj):
        """return customer email"""
        return obj.customer.email

    @admin.display(ordering="customer__platform", description="platform")
    def get_platform(self, obj):
        """return customer platform"""
        return obj.customer.platform
