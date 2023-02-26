"""OrderA Admin"""
from django.contrib import admin

from core.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Payment Admin"""
