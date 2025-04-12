from rest_framework import serializers
from .models import MeetingRequest, PublisherContact, PublisherRegister


class SavePublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherRegister
        fields = (
            # 'SortId',
            'PublisherId',
            'MediaName',
            'CompanyName',
            'TimeZone',
            'BusinessEmail',
            'OfficeLocation',
            'Country',
            'Website',
            'ContactName',
            'Position',
            'BusinessName',
            'MobileCode',
            'MobileNumber',
            'DefaultCurrency',
            'Status',
            'ContactsOnOff',
            'RegBy',
            'UserName',
            'PlanStatus',
            'PlanExpiryDate',
            'EnableMediaEntry',
            'EnableMailUpdates'
        )


class SavePublisherUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherRegister
        fields = (
            # 'SortId',
            'PublisherId',
            'UserName'
        )


class SavePublisherSEOSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherRegister
        fields = (
            # 'SortId',
            'PublisherId',
            # 'BannerImage',
            'UserName',
            'Description',
            'Title',
            'SeoDescription',
            'Keywords',
            'EnableBot',
            'BotName',
            'BotAavatar'
        )


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherRegister
        fields = (
            'SortId',
            'PublisherId',
            'MediaName',
            'CompanyName',
            'TimeZone',
            'BusinessEmail',
            'OfficeLocation',
            'Country',
            'Website',
            'ContactName',
            'Position',
            'BusinessName',
            'MobileCode',
            'MobileNumber',
            'DefaultCurrency',
            'Status',
            'ContactsOnOff',
            'RegBy',
            'ProfileImage',
            'UserName',
            'BannerImage',
            'BannerImageForMobile',
            'UserName',
            'Description',
            'Title',
            'SeoDescription',
            'Keywords',
            'PlanStatus',
            'PlanExpiryDate',
            'EnableBot',
            'BotName',
            'BotAavatar',
            'EnableMediaEntry',
            'EnableMailUpdates'
        )


class UploadPublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherRegister
        fields = (
            # 'SortId',
            'PublisherId',
            'CompanyName',
            'ProfileImage'
        )


class UploadPublisherBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherRegister
        fields = (
            # 'SortId',
            'PublisherId',
            'UserName',
            'BannerImage'
        )
class UploadPublisherBannerForMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherRegister
        fields = (
            # 'SortId',
            'PublisherId',
            'UserName',
            'BannerImageForMobile'
        )


class PublisherRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherRegister
        fields = (
            # 'SortId',
            'PublisherId',
            'BusinessEmail',
            'Status',
        )


class SavePublisherContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherContact
        fields = (
            # 'SortId',
            'PublisherContactId',
            'PublisherId',
            'Name',
            'Designation',
            'BioData',
            'Expertise',
            'Language',
            'Email',
            'PhoneNumber',
            'PhoneCode',
            'CountriesHandled',
            'LocationHandled',
            'TimeZone',
        )


class PublisherContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherContact
        fields = (
            # 'SortId',
            'PublisherContactId',
            'PublisherId',
            'Name',
            'Designation',
            'BioData',
            'Expertise',
            'Language',
            'Email',
            'PhoneNumber',
            'PhoneCode',
            'CountriesHandled',
            'LocationHandled',
            'TimeZone',
            'ProfileImage',
        )


class UploadPublisherContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherContact
        fields = (
            # 'SortId',
            'PublisherContactId',
            'Name',
            'ProfileImage'
        )


class SaveMeetingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRequest
        fields = (
            # 'SortId',
            'MeetingRequestId',
            'AdvertiserId',
            'PublisherId',
            'MediaId',
            'PublisherContactId',
            'PreferredContact',
            'HelpRequiredFor',
            'FromDate',
            'FromTime',
            'ToDate',
            'ToTime',
            'TimeZone',
            'Message',
            'CreatedDate',
            'Status'
        )
