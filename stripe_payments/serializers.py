from decimal import Decimal
from typing import Any

from django.core.validators import MinValueValidator
from rest_framework import serializers


class CheckoutItemSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(default=1)
    description = serializers.CharField()
    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.50"),
        validators=[MinValueValidator(Decimal("0.50"))],
    )


class CheckoutSessionRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    platform = serializers.CharField(max_length=30, default="lezing")
    currency = serializers.CharField(max_length=3, default="eur")
    line_items: Any = serializers.ListSerializer(child=CheckoutItemSerializer())
    success_url = serializers.URLField(default="http://127.0.0.1:8000/success/")
    cancel_url = serializers.URLField(default="http://127.0.0.1:8000/cancel/")
