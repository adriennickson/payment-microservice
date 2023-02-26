"""OrderA Admin"""
from django.contrib import admin

from core.models import OrderItem


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """OrderItem Admin"""
