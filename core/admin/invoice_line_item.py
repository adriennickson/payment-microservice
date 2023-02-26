"""OrderA Admin"""
from django.contrib import admin

from core.models import InvoiceLineItem


@admin.register(InvoiceLineItem)
class InvoiceLineItemAdmin(admin.ModelAdmin):
    """InvoiceLineItem Admin"""

    list_display = ("pk", "description", "amount")
