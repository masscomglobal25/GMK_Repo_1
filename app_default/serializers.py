from rest_framework import serializers
from .models import AdUnitCategory, AdvertiserAssistanceSupport, BotAavatar, CountryType, LightingType, OrganisationType, ServiceOrderUnit, ServiceUnitType, StaffPermission, TimeZone, UserType, Vertical, VerticalStatus


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ('SortId',
                  'UserTypeId',
                  'UserType')


class VerticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vertical
        fields = ('SortId',
                  'VerticalId',
                  'Identification',
                  'VerticalName',
                  'VerticalIcon',
                  'VerticalIconBW',
                  'VerticalImage',
                  'VerticalEmoji',
                  'VerticalOrder',
                  'VerticalCoverImage',
                  'VerticalCoverVideoLink',
                  'RefId')


class SaveVerticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vertical
        fields = ('SortId',
                  'VerticalId',
                  'Identification',
                  'VerticalName',
                  'VerticalOrder',
                  'VerticalCoverVideoLink',
                  'RefId')


class UploadVerticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vertical
        fields = (
            'VerticalId',
            'VerticalIcon',
            'VerticalIconBW',
            'VerticalImage',
            'VerticalEmoji',
            'VerticalCoverImage',
        )


class CountryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryType
        fields = ('SortId',
                  'CountryTypeId',
                  'CountryType')


class LightingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightingType
        fields = (
            'SortId',
            'LightingTypeId',
            'LightingType'
        )


class VerticalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerticalStatus
        fields = ('VerticalStatusId',
                  'VerticalStatus')


class AdUnitCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdUnitCategory
        fields = (
            'SortId',
            'AdUnitCategoryId',
            'AdUnitCategory',
            'OrderNo'
        )


class TimeZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeZone
        fields = (
            'SortId',
            'TimeZoneId',
            'TimeZone'
        )


class ServiceUnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceUnitType
        fields = (
            'SortId',
            'ServiceUnitTypeId',
            'ServiceUnitType'
        )


class ServiceOrderUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOrderUnit
        fields = (
            'SortId',
            'ServiceOrderUnitId',
            'ServiceOrderUnit'
        )


class StaffPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffPermission
        fields = (
            'SortId',
            'StaffPermissionId',
            'StaffPermission'
        )


class AdvertiserAssistanceSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertiserAssistanceSupport
        fields = (
            'SortId',
            'AssistanceId',
            'AssistanceIcon',
            'AssistanceName',
            'InfoLabel',
            'SupportBy',
            'CreditsRequired'
        )


class OrganisationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganisationType
        fields = (
            'SortId',
            'OrganisationTypeId',
            'OrganisationType'
        )


class BotAavatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotAavatar
        fields = (
            'SortId',
            'BotAavatarId',
            'BotAavatar'
        )
