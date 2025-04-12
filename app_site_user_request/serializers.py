from rest_framework import serializers
from .models import SiteRequest


class SiteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteRequest
        fields = (
            'SortId',
            'SiteRequestId',
            'UserTypeId',
            'UserId',
            'RequestType',
            'Heading',
            'Message',
            'CreatedDate',
        )
