from rest_framework import serializers

from app_ad_buzz.models import AdBuzz, AdBuzzImage


class AdBuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdBuzz
        fields = (
            'SortId',
            'AdBuzzId',
            'Content',
            'Heading',
            'UserId',
            'UserType',
            'CountrySelect',
            'AdbuzzCategory',
            'AdbuzzTagging',
            'UploadOption',
            'VideoLink',
            'LikeCount',
            'ShareCount',
            'ViewCount',
            'CreatedDate',
            'UpdatedDate',
            'EnableComment',
            'Status',
            'SeoTitle',
            'SeoDescription',
            'SeoKeywords',
            'LikedUser'
        )


class AdBuzzImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdBuzzImage
        fields = (
            'SortId',
            'AdBuzzImageId',
            'AdBuzzId',
            'AdBuzzImageName'
        )
