from rest_framework import serializers

from app_sales_marketing.models import SalesMarketing, SalesMarketingDetail


class SalesMarketingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesMarketing
        fields = (
            # 'SortId',
            'SalesMarketingId',
            'ConnectedTo',
            'CompanyName',
            'MediaName',
            'Country',
            'Email',
            'Phone',
            'IsAccountCreated',
            'ConnectedPersonId',
            'Status',
            'Health'
        )


class SalesMarketingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesMarketingDetail
        fields = (
            # 'SortId',
            'SalesMarketingDetailId',
            'SalesMarketingId',
            'UserId',
            'UserType',
            'ConnectedThrough',
            'ConnectedType',
            'MeetingFeedback',
            'DetailsShared',
            'Comments',
            'Status',
            'Health',
            'CreatedDate'
        )
