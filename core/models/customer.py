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
