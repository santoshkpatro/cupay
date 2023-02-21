from django.contrib import admin

from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "transaction_id",
        "merchant",
        "amount",
        "currency",
        "status",
        "created_at",
        "is_live_mode",
    )
    list_filter = ("is_live_mode",)
