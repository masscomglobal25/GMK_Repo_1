from rest_framework import serializers

from app_ai_external.models import AIFilteredData


class AIFilteredDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIFilteredData
        fields = (
            'SortId',
            'AIFilteredDataId',
            'UserId',
            'CityRegion',
            'Language',
            'Summary',
            'AIJsonData'
        )
