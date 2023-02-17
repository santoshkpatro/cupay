from django.contrib import admin

from .models import Merchant, Collaborator


class CollaboratorInline(admin.StackedInline):
    model = Collaborator
    extra = 1


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = (
        "merchant_id",
        "company_name",
        "is_verified",
        "virtual_balance_curreny",
        "virtual_balance",
    )
    inlines = (CollaboratorInline,)


@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ("merchant", "user", "role")
