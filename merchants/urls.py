from django.urls import path, include

urlpatterns = [
    path("<str:merchant_id>/payments/", include("merchants.payments.urls")),
]
