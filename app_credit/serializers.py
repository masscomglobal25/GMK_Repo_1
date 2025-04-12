from rest_framework import serializers

from app_credit.models import AdvertiserCreditRequest, Credits


class CreditsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credits
        fields = (
            'SortId',
            'CreditId',
            'CreditCount',
            'Amount'
        )

class AdvertiserCreditRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertiserCreditRequest
        fields = (
            'SortId',
            'CreditRequiredId',
            'AdvertiserId',
            'CreditsRequired',
            'TotalPayable',
            'Status'
        )
