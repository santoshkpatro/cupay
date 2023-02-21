import uuid
from django.db import models

from base.models import BaseModel
from merchants.models import Merchant


class Transaction(BaseModel):
    class Status(models.TextChoices):
        CREATED = ("created", "CREATED")
        ATTEMPTED = ("attempted", "ATTEMPTED")
        PAID = ("paid", "PAID")

    class Currency(models.TextChoices):
        INR = ("INR", "INR")
        USD = ("USD", "USD")

    is_live_mode = models.BooleanField(default=True, db_index=True)
    merchant = models.ForeignKey(
        Merchant, on_delete=models.SET_NULL, related_name="orders", null=True
    )
    transaction_id = models.CharField(
        max_length=50, blank=True, unique=True, editable=False
    )
    amount = models.PositiveIntegerField()
    currency = models.CharField(max_length=3, choices=Currency.choices)
    attempts = models.PositiveIntegerField(default=0)
    status = models.CharField(
        choices=Status.choices, default=Status.CREATED, max_length=10
    )
    notes = models.JSONField(blank=True, null=True)
    receipt = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = "transactions"

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = f"trans_{uuid.uuid4().hex}"
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.transaction_id
