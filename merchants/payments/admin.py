from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "payment_id",
        "amount",
        "currency",
        "status",
        "payment_method",
        "refund_status",
        "created_at",
        "is_live_mode",
    )
