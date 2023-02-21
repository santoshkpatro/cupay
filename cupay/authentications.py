import base64
from rest_framework import authentication
from rest_framework import exceptions

from merchants.models import Merchant


class MerchantAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        headers = request.META.get("HTTP_AUTHORIZATION")
        if not headers:
            raise exceptions.AuthenticationFailed("Authentication required")

        auth = headers.split()

        if not len(auth) == 2 and auth[0].lower() == "basic":
            raise exceptions.AuthenticationFailed("Authentication Method not allowed")

        username, password = base64.b64decode(auth[1]).decode("utf-8").split(":")

        try:
            merchant: Merchant = Merchant.objects.get(
                live_merchant_access_key=username,
                live_merchant_access_id=password,
            )
        except Merchant.DoesNotExist:
            raise exceptions.AuthenticationFailed("Authentication Failed")

        request.merchant = merchant