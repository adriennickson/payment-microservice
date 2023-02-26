from django.db import models

from .account import Account
from .invoice import Invoice
from .payment import Payment


class FinancialTransaction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE, null=True)
    invoice = models.ForeignKey(to=Invoice, on_delete=models.CASCADE, null=True)
    payment = models.ForeignKey(to=Payment, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)
