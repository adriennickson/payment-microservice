from django.db import models

from .invoice import Invoice
from .order_item import OrderItem


class InvoiceLineItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_item = models.OneToOneField(
        to=OrderItem, on_delete=models.CASCADE, primary_key=True
    )
    invoice = models.ForeignKey(to=Invoice, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)
    amount = models.FloatField()
