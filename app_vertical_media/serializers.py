from rest_framework import serializers
from .models import Media, MediaAdType, MediaAdTypeImage


class SaveMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = (
            # 'SortId',
            'Identification',
            'MediaId',
            'VerticalType',
            'MediaName',
            'Category',
            'PrimaryLanguage',
            'TimeZone',
            'MediaManagedBy',
            'WebsiteLink',
            'WebStatsOnOff',
            'EventVenue',
            'PublisherId',
            'CountryEvent',
            'ContactPerson',
            'CityRegion',
            'Language',
            'MediaCategory',
            'EstimateReached',
            'BenefitsOfAdvertising',
            'PromoVideoLink',
            'MapLink',
            'Latitude',
            'Longitude',
            'IsHyperlocal',
            'Availability',
            'Status',
            'ViewsCount',
            'RecommendedMedia',
            'ShowOnOff',
            'ViewOnlyMediaStore',
            'ModifiedDate',
            'SEOMetaTitle',
            'SEOMetaDescription',
            'SEOMetaKeyword',
            'CountryEventJSON',
            'CityRegionJSON',
            'LanguageJSON',
            'SEOMetaKeywordJSON',
            'BenefitsOfAdvertisingNonHTML')


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = (
            'SortId',
            'Identification',
            'MediaId',
            'VerticalType',
            'MediaName',
            'Category',
            'PrimaryLanguage',
            'TimeZone',
            'MediaManagedBy',
            'WebsiteLink',
            'WebStatsOnOff',
            'EventVenue',
            'PublisherId',
            'CountryEvent',
            'ContactPerson',
            'CityRegion',
            'Language',
            'MediaCategory',
            'EstimateReached',
            'BenefitsOfAdvertising',
            'PromoVideoLink',
            'MediaKit',
            'MapLink',
            'Latitude',
            'Longitude',
            'IsHyperlocal',
            'Availability',
            'MediaImage',
            'Status',
            'ViewsCount',
            'ShowOnOff',
            'ViewOnlyMediaStore',
            'RecommendedMedia',
            'ModifiedDate',
            'SEOMetaTitle',
            'SEOMetaDescription',
            'SEOMetaKeyword',
            'CountryEventJSON',
            'CityRegionJSON',
            'LanguageJSON',
            'SEOMetaKeywordJSON',
            'BenefitsOfAdvertisingNonHTML'
        )


class FilterMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = (
            # 'SortId',
            'MediaId',
            'Identification',
            'VerticalType',
            'CountryEvent',
            'MediaName',
            'MediaManagedBy',
            'ViewOnlyMediaStore',
            'Status',
        )


class UploadMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = (
            'SortId',
            'MediaId',
            'MediaName',
            'MediaImage',
            'MediaKit'
        )

# class UploadMediaImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MediaImage
#         fields = (
#             'SortId',
#             'MediaImageId',
#             'MediaId',
#             'MediaImage'
#         )


class SaveMediaAdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAdType
        fields = (
            # 'SortId',
            'Identification',
            'MediaAdTypeId',
            'MediaId',
            'Size',
            'OutdoorSize',
            'CreativeSize',
            'AdFormat',
            'NumberOfSpots',
            'ProgramStartTime',
            'ProgramEndTime',
            'OrderUnit',
            'UnitType',
            'OrderingQuantity',
            'CreativesRequired',
            'Position',
            'DigitalPosition',
            'SpecificCategory',
            'MediaAdType',
            'SiteName',
            'LocationType',
            'VerticalTypeId',
            'NoOfScreen',
            'MediaAdUnitDescription',
            'IsDigital',
            'SingleRotationTime',
            'DurationOfCreative',
            'Availability',
            'PackageName',
            'PackageType',
            'StartDate',
            'EndDate',
            'NoOfDays',
            'PromoVideoLink',
            'Currency',
            'MonthlyRentalRate',
            'Discount',
            'NetCostBeforeTax',
            'ProductionCost',
            'Tax',
            'NetCost',
            'RateValidaty',
            'CostPerThousandDisplay',
            'CostPerThousand',
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
            'MediaAdTypeImage',
            'TermsAndConditions',
            'ShowOnOff',
            'Status',
            'RateDisplay',
            'PriceRangeNote',
            'AvailabilityJSON',
            'NearByAdvantagesJSON',
            'MatchingCategoriesJSON',
            'AgeGroupJSON',
            'GenderGroupJSON',
            'IncomeGroupJSON',
            'MediaAdUnitDescriptionNonHTML',
            'TermsAndConditionsNonHTML'
        )


class MediaAdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAdType
        fields = (
            'SortId',
            'Identification',
            'MediaAdTypeId',
            'MediaId',
            'Size',
            'OutdoorSize',
            'CreativeSize',
            'AdFormat',
            'NumberOfSpots',
            'PromoAudio',
            'ProgramStartTime',
            'ProgramEndTime',
            'OrderUnit',
            'UnitType',
            'OrderingQuantity',
            'CreativesRequired',
            'Position',
            'DigitalPosition',
            'MediaAdType',
            'SiteName',
            'SpecificCategory',
            'LocationType',
            'VerticalTypeId',
            'NoOfScreen',
            'MediaAdUnitDescription',
            'IsDigital',
            'SingleRotationTime',
            'DurationOfCreative',
            'Availability',
            'PackageName',
            'PackageType',
            'StartDate',
            'EndDate',
            'NoOfDays',
            'PromoVideoLink',
            'Currency',
            'MonthlyRentalRate',
            'Discount',
            'NetCostBeforeTax',
            'ProductionCost',
            'Tax',
            'NetCost',
            'RateValidaty',
            'CostPerThousandDisplay',
            'CostPerThousand',
            'AdUnitCategory',
            'AdTypeMediaKit',
            'ThumbnailImage',
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
            'MediaAdTypeImage',
            'TermsAndConditions',
            'ShowOnOff',
            'Status',
            'RateDisplay',
            'PriceRangeNote',
            'AvailabilityJSON',
            'NearByAdvantagesJSON',
            'MatchingCategoriesJSON',
            'AgeGroupJSON',
            'GenderGroupJSON',
            'IncomeGroupJSON',
            'MediaAdUnitDescriptionNonHTML',
            'TermsAndConditionsNonHTML'
        )


class AllMediaAdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAdType
        fields = (
            'MediaAdTypeId',
            'MediaAdType',
            'SiteName',
            'PackageName',
            'ShowOnOff',
            'Status',
        )


class UploadMediaAdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAdType
        fields = (
            # 'SortId',
            'MediaAdTypeId',
            'MediaId',
            'Size',
            'OutdoorSize',
            'CreativeSize',
            'AdFormat',
            'NumberOfSpots',
            'PromoAudio',
            'ProgramStartTime',
            'ProgramEndTime',
            'OrderUnit',
            'UnitType',
            'OrderingQuantity',
            'CreativesRequired',
            'Position',
            'DigitalPosition',
            'MediaAdType',
            'SiteName',
            'LocationType',
            'VerticalTypeId',
            'NoOfScreen',
            'MediaAdUnitDescription',
            'IsDigital',
            'SingleRotationTime',
            'DurationOfCreative',
            'Availability',
            'PackageName',
            'PackageType',
            'StartDate',
            'EndDate',
            'NoOfDays',
            'PromoVideoLink',
            'Currency',
            'MonthlyRentalRate',
            'Discount',
            'NetCostBeforeTax',
            'ProductionCost',
            'Tax',
            'NetCost',
            'RateValidaty',
            'AdUnitCategory',
            'AdTypeMediaKit',
            'ThumbnailImage',
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
            'MediaAdTypeImage',
            'TermsAndConditions',
        )


class UploadMediaAdTypeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAdTypeImage
        fields = (
            'SortId',
            'MediaAdTypeImageId',
            'MediaAdTypeId',
            'MediaAdTypeImage',
            'OrderNo'
        )
