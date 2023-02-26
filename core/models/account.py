from django.db import models

from .customer import Customer


class Account(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.email} - {self.customer.platform}"
