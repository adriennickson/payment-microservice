from django.db import models

from .order import Order


class Invoice(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
