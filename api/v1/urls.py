from django.urls import re_path

from .transactions.views import (
    TransactionInitiateView,
    TransactionDetailView,
    TransactionListView,
)

urlpatterns = [
    re_path(r"^transactions/initiate/?$", TransactionInitiateView.as_view()),
    re_path(r"^transactions/?$", TransactionListView.as_view()),
    re_path(
        r"^transactions/(?P<transaction_id>[^/]+)/?$", TransactionDetailView.as_view()
    ),
]
