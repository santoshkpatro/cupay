import uuid
import shortuuid
from django.db import models
from django.db import transaction

from core.base.models import BaseModel
from core.users.models import User


class Merchant(BaseModel):
    class BusinessCountry(models.TextChoices):
        INDIA = ("IND", "India")
        USA = ("USA", "United State of America")

    class VirtualBalanceCurrency(models.TextChoices):
        INR = ("INR", "INR")
        USD = ("USD", "USD")

    merchant_id = models.CharField(max_length=50, unique=True, editable=False)
    company_name = models.CharField(max_length=300)
    company_description = models.TextField(blank=True, null=True)
    company_logo = models.ImageField(
        upload_to="merchants/logos/", blank=True, null=True
    )
    is_registered = models.BooleanField(default=False)
    business_country = models.CharField(max_length=3, choices=BusinessCountry.choices)
    business_description = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    # Balance
    virtual_balance_curreny = models.CharField(
        max_length=3, choices=VirtualBalanceCurrency.choices
    )
    virtual_balance = models.DecimalField(max_digits=12, decimal_places=4, default=0)

    # Live Keys
    live_merchant_access_key = models.CharField(
        blank=True, null=True, unique=True, max_length=50
    )
    live_merchant_access_id = models.CharField(blank=True, null=True, max_length=50)

    # Test Keys
    test_merchant_access_key = models.CharField(
        blank=True, null=True, unique=True, max_length=50
    )
    test_merchant_access_id = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "merchants"

    def __str__(self) -> str:
        return self.company_name

    def save(self, *args, **kwargs):
        if not self.merchant_id:
            self.merchant_id = shortuuid.ShortUUID().random(10)
        return super().save(*args, **kwargs)

    @transaction.atomic
    def generate_live_merchant_credentials(self):
        self.live_merchant_access_key = f"live_{uuid.uuid4().hex}"
        self.live_merchant_access_id = uuid.uuid4().hex

        self.save()

    @transaction.atomic
    def generate_test_merchant_credentials(self):
        self.test_merchant_access_key = f"test_{uuid.uuid4().hex}"
        self.test_merchant_access_id = uuid.uuid4().hex

        self.save()


class Collaborator(BaseModel):
    class Role(models.TextChoices):
        OWNER = ("owner", "Owner")
        ADMIN = ("admin", "Admin")
        STAFF = ("staff", "Staff")

    merchant = models.ForeignKey(
        Merchant, on_delete=models.CASCADE, related_name="merchant_collaborators"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_collaborators"
    )
    role = models.CharField(max_length=5, choices=Role.choices)

    class Meta:
        db_table = "collaborators"

    def __str__(self) -> str:
        return str(self.id)
