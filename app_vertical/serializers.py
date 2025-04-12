from rest_framework import serializers
from .models import OutOfHome, OutOfHomeImage, OutOfHomeMediaAdType, OutOfHomeMediaAdTypeImage


class SaveOutOfHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutOfHome
        fields = (
            # 'SortId',
            'OutOfHomeId',
            'SiteOwnerName',
            'PublisherId',
            'CountryEvent',
            'CityRegion',
            'Location',
            'Size',
            'Language',
            'EstimateReached',
            'BenefitsOfAdvertising',
            'PromoVideoLink',
            'Availability',
            'MapLink',
            'Latitude',
            'Longitude',
            'IsHyperlocal',
            'Status',
            'ViewsCount',
            'ModifiedDate')


class OutOfHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutOfHome
        fields = (
            # 'SortId',
            'OutOfHomeId',
            'SiteOwnerName',
            'PublisherId',
            'CountryEvent',
            'CityRegion',
            'Location',
            'Size',
            'Language',
            'EstimateReached',
            'BenefitsOfAdvertising',
            'PromoVideoLink',
            'Availability',
            'MediaKit',
            'MapLink',
            'Latitude',
            'Longitude',
            'IsHyperlocal',
            'Status',
            'ViewsCount',
            'ModifiedDate',
            'OutOfHomeImage'
        )


class UploadOutOfHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutOfHome
        fields = (
            'SortId',
            'OutOfHomeId',
            'SiteOwnerName',
            'OutOfHomeImage',
            'MediaKit'
        )

# class UploadOutOfHomeImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OutOfHomeImage
#         fields = (
#             'SortId',
#             'OutOfHomeImageId',
#             'OutOfHomeId',
#             'OutOfHomeImage'
#         )


class SaveOutOfHomeMediaAdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutOfHomeMediaAdType
        fields = (
            # 'SortId',
            'OutOfHomeMediaAdTypeId',
            'OutOfHomeId',
            'MediaAdType',
            'SiteName',
            'LocationType',
            'VerticalTypeId',
            'NoOfScreen',
            'IsDigital',
            'LightingType',
            'MediaAdUnitDescription',
            'PackageName',
            'PackageType',
            'StartDate',
            'EndDate',
            'NoOfDays',
            'MonthlyRentalRate',
            'Discount',
            'NetCostBeforeTax',
            'ProductionCost',
            'Tax',
            'NetCost',
            'RateValidaty',
            'PromoVideoLink',
            'Availability',
            'AdUnitCategory',
            'AdTypeEstimateReached',
            'NearByAdvantages',
            'MatchingCategories',
            'AgeGroup',
            'GenderGroup',
            'IncomeGroup',
            'NationalityCommunity',
            'RunAsOffer',
            'IsLocalTaxApplied',
            'IsNeedApproval',
            'NoOfDaysRequired',
            'TermsAndConditions',
            'SingleRotationTime',
            'DurationOfCreative',
        )


class OutOfHomeMediaAdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutOfHomeMediaAdType
        fields = (
            # 'SortId',
            'OutOfHomeMediaAdTypeId',
            'OutOfHomeId',
            'MediaAdType',
            'SiteName',
            'LocationType',
            'VerticalTypeId',
            'NoOfScreen',
            'MediaAdUnitDescription',
            'IsDigital',
            'LightingType',
            'PackageName',
            'PackageType',
            'StartDate',
            'EndDate',
            'NoOfDays',
            'MonthlyRentalRate',
            'Discount',
            'NetCostBeforeTax',
            'ProductionCost',
            'Tax',
            'NetCost',
            'RateValidaty',
            'AdTypeMediaKit',
            'PromoVideoLink',
            'Availability',
            'AdUnitCategory',
            'AdTypeEstimateReached',
            'NearByAdvantages',
            'MatchingCategories',
            'AgeGroup',
            'GenderGroup',
            'IncomeGroup',
            'NationalityCommunity',
            'RunAsOffer',
            'IsLocalTaxApplied',
            'IsNeedApproval',
            'NoOfDaysRequired',
            'TermsAndConditions',
            'SingleRotationTime',
            'DurationOfCreative',
        )


class UploadOutOfHomeMediaAdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutOfHomeMediaAdType
        fields = (
            # 'SortId',
            'OutOfHomeMediaAdTypeId',
            'OutOfHomeId',
            'MediaAdType',
            'SiteName',
            'LocationType',
            'VerticalTypeId',
            'NoOfScreen',
            'IsDigital',
            'MediaAdUnitDescription',
            'LightingType',
            'PackageName',
            'PackageType',
            'StartDate',
            'EndDate',
            'NoOfDays',
            'MonthlyRentalRate',
            'Discount',
            'NetCostBeforeTax',
            'ProductionCost',
            'Tax',
            'NetCost',
            'RateValidaty',
            'AdTypeMediaKit',
            'AdUnitCategory',
            'AdTypeEstimateReached',
            'NearByAdvantages',
            'MatchingCategories',
            'AgeGroup',
            'GenderGroup',
            'IncomeGroup',
            'NationalityCommunity',
            'RunAsOffer',
            'IsLocalTaxApplied',
            'IsNeedApproval',
            'NoOfDaysRequired',
            'TermsAndConditions',
            'SingleRotationTime',
            'DurationOfCreative',
        )

class UploadOutOfHomeMediaAdTypeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutOfHomeMediaAdTypeImage
        fields = (
            'SortId',
            'OutOfHomeMediaAdTypeImageId',
            'OutOfHomeMediaAdTypeId',
            'OutOfHomeMediaAdTypeImage'
        )