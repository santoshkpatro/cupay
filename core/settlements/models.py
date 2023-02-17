import uuid
from django.db import models

from core.base.models import BaseModel
from core.merchants.models import Merchant


class Settlement(BaseModel):
    class Status(models.TextChoices):
        SCHEDULED = ("scheduled", "Scheduled")
        IN_PROGRESS = ("in_progress", "In Progress")
        COMPLETE = ("complete", "Complete")
        SKIPPED = ("skipped", "Skipped")
        FAILED = ("failed", "Failed")
        CANCELLED = ("cancelled", "Cancelled")

    merchant = models.ForeignKey(
        Merchant, on_delete=models.SET_NULL, related_name="settlements", null=True
    )
    settlement_id = models.CharField(max_length=50, unique=True, blank=True)
    amount = models.PositiveIntegerField()
    currency = models.CharField(max_length=3)
    scheduled_on = models.DateTimeField()
    status = models.CharField(max_length=15, choices=Status.choices)
    is_reschduled = models.BooleanField(default=False)

    class Meta:
        db_table = "settlements"

    def __str__(self) -> str:
        return self.settlement_id

    def save(self, *args, **kwargs):
        if not self.settlement_id:
            self.settlement_id = f"settlement_{uuid.uuid4().hex}"
        return super().save(*args, **kwargs)