from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'SortId',
            'AdvertiserId',
            'FirstName',
            'LastName',
            'BusinessEmail',
            'CompanyName',
            'BuildingNo',
            'StreetAddress',
            'City',
            'State',
            'ZIPCode',
            'Country',
            'PhoneNumber',
            'PhoneCode',
            'TargetCountries',
            'OrganisationType',
            'TargetAudience',
            'ProfileImage',
            'SMPicture',
            'Status',
            'Credits',
            'CreditsExpiryDate',
            'IsUpgrade',
            'EnableMailUpdates'
        )

class SaveProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            # 'SortId',
            'AdvertiserId',
            'FirstName',
            'LastName',
            'BusinessEmail',
            'CompanyName',
            'BuildingNo',
            'StreetAddress',
            'City',
            'State',
            'ZIPCode',
            'Country',
            'PhoneNumber',
            'PhoneCode',
            'TargetCountries',
            'OrganisationType',
            'TargetAudience',
            'Status',
            'Credits',
            'CreditsExpiryDate',
            'IsUpgrade',
            'EnableMailUpdates'
        )


class UploadProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            # 'SortId',
            'AdvertiserId',
            'CompanyName',
            'ProfileImage',
        )


class ProfileRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            # 'SortId',
            'AdvertiserId',
            'BusinessEmail',
            'Status',
            'Credits',
            'CreditsExpiryDate'
        )
