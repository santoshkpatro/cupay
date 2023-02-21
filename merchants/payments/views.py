from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from merchants.mixins import MerchantAuthMixin

from .models import Payment


class PaymentListView(LoginRequiredMixin, MerchantAuthMixin, View):
    def get(self, request, *args, **kwargs):
        payments = Payment.objects.filter(merchant=request.merchant).select_related(
            "transaction"
        )
        print(payments)
        return render(request, "merchants/payments/list.html", {"payments": payments})
