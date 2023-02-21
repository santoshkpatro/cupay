import uuid
from django.db import models

from base.models import BaseModel
from merchants.models import Merchant
from merchants.transactions.models import Transaction


class Payment(BaseModel):
    class Status(models.TextChoices):
        CREATED = ("created", "Created")
        AUTHORIZED = ("authorized", "Authorized")
        CAPTURED = ("captured", "Captured")
        REFUNDED = ("refunded", "Refunded")
        FAILED = ("failed", "Failed")

    class PaymentMethod(models.TextChoices):
        CARD = ("card", "Card")
        NET_BANKING = ("net_banking", "Net Banking")
        WALLET = ("wallet", "Wallet")
        UPI = ("upi", "UPI")
        UNKNOWN = ("unknown", "Unknown")

    class RefundStatus(models.TextChoices):
        PARTIAL = ("partial", "Partial")
        FULL = ("full", "Full")

    class CardType(models.TextChoices):
        DEBIT = ("debit", "Debit")
        CREDIT = ("credit", "Credit")
        UNKNOWN = ("unknown", "Unknown")

    class Currency(models.TextChoices):
        INR = ("INR", "INR")
        USD = ("USD", "USD")

    is_live_mode = models.BooleanField(default=True, db_index=True)
    merchant = models.ForeignKey(
        Merchant, on_delete=models.SET_NULL, null=True, related_name="payments"
    )
    payment_id = models.CharField(max_length=50, unique=True, blank=True, editable=False)
    transaction = models.ForeignKey(Transaction, on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField()
    currency = models.CharField(max_length=3, choices=Currency.choices)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.CREATED
    )
    payment_method = models.CharField(
        max_length=15, choices=PaymentMethod.choices, default=PaymentMethod.UNKNOWN
    )
    description = models.TextField(blank=True, null=True)
    is_international = models.BooleanField(default=False)
    is_captured = models.BooleanField(default=False)
    notes = models.JSONField(blank=True, null=True)
    bank = models.CharField(max_length=10, blank=True, null=True)
    vpa = models.CharField(max_length=100, blank=True, null=True)
    wallet = models.CharField(max_length=50, blank=True, null=True)

    service_charges = models.PositiveIntegerField(blank=True, null=True)

    # Card
    card_holder_name = models.CharField(max_length=150, blank=True, null=True)
    card_last_digits = models.IntegerField(blank=True, null=True)
    card_network = models.CharField(max_length=50, blank=True, null=True)
    card_type = models.CharField(
        max_length=10, choices=CardType.choices, blank=True, null=True
    )
    card_issuer_bank = models.CharField(max_length=10, blank=True, null=True)

    # Errors
    error_code = models.CharField(max_length=20, blank=True, null=True)
    error_source = models.CharField(max_length=10, blank=True, null=True)
    error_step = models.CharField(max_length=20, blank=True, null=True)

    # Refund
    refund_status = models.CharField(
        max_length=10, blank=True, null=True, choices=RefundStatus.choices
    )
    refund_amount = models.PositiveIntegerField(blank=True, null=True)
    refunded_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "payments"

    def __str__(self) -> str:
        return self.payment_id

    def save(self, *args, **kwargs):
        if not self.payment_id:
            self.payment_id = f"pay_{uuid.uuid4().hex}"
        return super().save(*args, **kwargs)
