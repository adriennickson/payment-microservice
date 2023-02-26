"""OrderA Admin"""
from django.contrib import admin

from core.models import FinancialTransaction


@admin.register(FinancialTransaction)
class FinancialTransactionAdmin(admin.ModelAdmin):
    """FinancialTransaction Admin"""
