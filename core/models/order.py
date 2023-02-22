from django.db import models

from .customer import Customer


class Order(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
