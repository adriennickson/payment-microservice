"""OrderA Admin"""
from django.contrib import admin
from django.db.models import Sum

from core.models import InvoiceLineItem, Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """OrderA Admin"""

    list_display = ("pk", "get_email", "get_platform", "get_amount")
    search_fields = ("get_email", "get_platform")

    @admin.display(ordering="customer__email", description="email")
    def get_email(self, obj):
        """return customer email"""
        return obj.customer.email

    @admin.display(ordering="customer__platform", description="platform")
    def get_platform(self, obj):
        """return customer platform"""
        return obj.customer.platform

    @admin.display(description="Amount")
    def get_amount(self, obj):
        """return amount of order"""
        amount = InvoiceLineItem.objects.filter(order_item__order=obj).aggregate(
            Sum("amount")
        )["amount__sum"]
        return amount
