from rest_framework import serializers
from .models import StaffRegister


class StaffRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffRegister
        fields = (
            # 'SortId',
            'StaffRegisterId',
            'Name',
            'EmailId',
            'StaffCode',
            'Address',
            'PinCode',
            'Phone',
            'Permission'
        )
