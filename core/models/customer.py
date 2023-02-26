import uuid

from django.db import models


class ClientPlatform(models.TextChoices):
    EKWALI = "EKWALI"
    LEZIN = "Lezin"
    IMMO237 = "237Immo"
    EWII = "E-wii"
    AFRIQUEPROFONDE = "Afrique Profonde"
    INSIDEMENOUA = "Inside Menoua"
    TRIBALLUXURY = "Tribal Luxury"


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    platform = models.CharField(max_length=16, choices=ClientPlatform.choices)

    def __str__(self):
        return f"{self.email} - {self.platform}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["email", "platform"], name="unique_customer"
            )
        ]
