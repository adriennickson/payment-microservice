from rest_framework import serializers

from core.models import Account

from .customer import CustomerSerializer


class AccountSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Account
        fields = ["created_at", "updated_at", "customer"]
