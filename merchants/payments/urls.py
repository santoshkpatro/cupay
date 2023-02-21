from django.urls import path
from . import views

urlpatterns = [
    path("", views.PaymentListView.as_view(), name="list")
]