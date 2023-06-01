from django.shortcuts import render  # noqa
from rest_framework.viewsets import ModelViewSet

from core.models import Account
from core.serializers import AccountSerializer


# Create your views here.
class AccountViewset(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
