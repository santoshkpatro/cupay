from django.db import models

from base.models import BaseModel
from merchants.models import Merchant
from users.models import User


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
        unique_together = ["merchant", "user"]

    def __str__(self) -> str:
        return str(self.id)
