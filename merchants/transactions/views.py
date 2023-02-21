from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class TransactionListView(LoginRequiredMixin, View):
    def get(self, request, merchant_id):
        return render(request, "merchants/transactions/list.html")