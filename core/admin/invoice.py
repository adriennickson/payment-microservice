"""OrderA Admin"""
from django.contrib import admin
from django.db.models import Sum

from core.models import FinancialTransaction, Invoice, InvoiceLineItem


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    """Invoice Admin"""

    list_display = ("pk", "get_email", "get_platform", "get_amount", "get_remaining")
    search_fields = ("get_email", "get_platform")

    @admin.display(ordering="customer__email", description="email")
    def get_email(self, obj):
        """return customer email"""
        return obj.order.customer.email

    @admin.display(ordering="customer__platform", description="platform")
    def get_platform(self, obj):
        """return customer platform"""
        return obj.order.customer.platform

    @admin.display(description="Amount")
    def get_amount(self, obj):
        """return amount of order"""
        amount = InvoiceLineItem.objects.filter(order_item__order=obj.order).aggregate(
            Sum("amount")
        )["amount__sum"]
        return amount

    @admin.display(description="Remaining")
    def get_remaining(self, obj):
        """return invoice remaining"""
        amount = self.get_amount(obj)
        payed = (
            FinancialTransaction.objects.select_related("payment")
            .filter(invoice__order=obj.order)
            .aggregate(Sum("payment__amount"))["payment__amount__sum"]
        )
        return amount - payed
