from django.core.exceptions import PermissionDenied
from django.http import Http404

from .models import Merchant
from .collaborators.models import Collaborator


class MerchantAuthMixin:
    def dispatch(self, request, *args, **kwargs):
        merchant_id = kwargs["merchant_id"]
        try:
            merchant = Merchant.objects.get(merchant_id=merchant_id)
        except Merchant.DoesNotExist:
            raise Http404

        request.merchant = merchant

        try:
            collaborator = Collaborator.objects.get(merchant=merchant, user=request.user)
        except Collaborator.DoesNotExist:
            raise Http404

        return super().dispatch(request, *args, **kwargs)
