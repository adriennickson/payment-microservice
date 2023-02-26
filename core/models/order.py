import uuid

from django.db import models

from .customer import Customer


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
