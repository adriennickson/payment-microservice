from django.db import models


class TransactionType(models.Model):
    code = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.code}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["code"], name="unique_transaction_type")
        ]
