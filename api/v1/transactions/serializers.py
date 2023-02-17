from rest_framework import serializers


class TransactionCreateSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    currency = serializers.CharField()
