import base64
from rest_framework.views import APIView
from rest_framework.response import Response

from core.transactions.models import Transaction
from core.merchants.models import Merchant

from .serializers import TransactionCreateSerializer
from cupay.authentications import MerchantAuthentication

class TransactionInitiateView(APIView):
    def get_merchant(self, request) -> Merchant:
        return

    def post(self, request):
        print(request)
        return Response(data={"message": "Ok"})


class TransactionListView(APIView):
    authentication_classes = [MerchantAuthentication]

    def get(self, request):
        return Response(data={})


class TransactionDetailView(APIView):
    def get(sef, request, transaction_id):
        return Response(data={"message": transaction_id})