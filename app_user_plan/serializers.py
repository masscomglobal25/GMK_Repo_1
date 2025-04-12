from rest_framework import serializers
from .models import UserSitePlan, UserSitePlanItem


class UserSitePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSitePlan
        fields = (
            # 'SortId',
            'SitePlanId',
            'PlanName',
            'PlanDetails',
            'UserTypeId',
            'Validity',
            'Currency',
            'Amount',
            'Credit',
            'Status',
            'OpportunityCountInPlan'
        )

class UserSitePlanItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSitePlanItem
        fields = (
            # 'SortId',
            'SitePlanItemId',
            'ItemName',
            'Status',
        )
