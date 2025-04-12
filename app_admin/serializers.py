from rest_framework import serializers
from .models import AdBuzzCategory, AdBuzzTagging, AdFormat, AdUnitSpecificCategory, AdunitPosition, AdunitSize, AgeGroup, BrandCategory, CampaignObjective, CampaignUnit, CityRegion, Continent, CountryEvent, EstimatedReach, GenderGroup, HelpRequiredFor, HighlyRecommendedMedia, IncomeGroup, Language, Location, LocationType, MatchingCategory, MediaCategory, MeetingRequest, NationalityCommunity, NearByAdvantage, RecommendationBanner, SiteBanner, SiteMenu, VerticalType


class SaveMatchingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchingCategory
        fields = (
            # 'SortId',
            'MatchingCategoryId',
            'Identification',
            'MatchingCategory',
            'Enable',
        )


class MatchingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchingCategory
        fields = (
            # 'SortId',
            'MatchingCategoryId',
            'Identification',
            'MatchingCategory',
            'CategoryIcon',
            'Enable'
        )


class UploadMatchingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchingCategory
        fields = (
            'SortId',
            'MatchingCategoryId',
            'MatchingCategory',
            'CategoryIcon',
        )


class NationalityCommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = NationalityCommunity
        fields = (
            'SortId',
            'NationalityCommunityId',
            'NationalityCommunity'
        )


class SaveIncomeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeGroup
        fields = (
            # 'SortId',
            'IncomeGroupId',
            'IncomeGroup',
        )


class IncomeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeGroup
        fields = (
            # 'SortId',
            'IncomeGroupId',
            'IncomeGroup',
            'IncomeGroupIcon',
        )


class UploadIncomeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeGroup
        fields = (
            'SortId',
            'IncomeGroupId',
            'IncomeGroup',
            'IncomeGroupIcon',
        )


class SaveAgeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeGroup
        fields = (
            # 'SortId',
            'AgeGroupId',
            'AgeGroup',
        )


class AgeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeGroup
        fields = (
            # 'SortId',
            'AgeGroupId',
            'AgeGroup',
            'AgeGroupIcon',
        )


class UploadAgeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeGroup
        fields = (
            'SortId',
            'AgeGroupId',
            'AgeGroup',
            'AgeGroupIcon',
        )


class SaveGenderGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderGroup
        fields = (
            # 'SortId',
            'GenderGroupId',
            'GenderGroup',
        )


class GenderGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderGroup
        fields = (
            # 'SortId',
            'GenderGroupId',
            'GenderGroup',
            'GenderGroupIcon',
        )


class UploadGenderGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderGroup
        fields = (
            'SortId',
            'GenderGroupId',
            'GenderGroup',
            'GenderGroupIcon',
        )


class LocationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationType
        fields = (
            'SortId',
            'LocationTypeId',
            'LocationType'
        )


class EstimatedReachSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstimatedReach
        fields = (
            'SortId',
            'EstimatedReachId',
            'EstimatedReach',
            'ReachFrom',
            'ReachTo',
            'AverageReach'
        )


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = (
            'SortId',
            'LanguageId',
            'Language'
        )

class AdBuzzTaggingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdBuzzTagging
        fields = (
            'SortId',
            'AdBuzzTaggingId',
            'AdBuzzTagging'
        )


class VerticalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerticalType
        fields = (
            'SortId',
            'VerticalId',
            'VerticalTypeId',
            'VerticalType'
        )


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = (
            # 'SortId',
            'ContinentId',
            'Continent',
            'ContinentOnOFF',
            'OrderNo'
        )


class SaveCountryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryEvent
        fields = (
            # 'SortId',
            'CountryEventId',
            'Identification',
            'CountryType',
            'ContinentId',
            'CountryEventName',
            'CountryCode',
            'CountryNumericCode',
            'CountryTag',
            'TelephoneCode',
            'Description',
            'StartDate',
            'EndDate',
            'MatchingCategoriesToAd',
            'GeneralInfo',
            'AvailableVertical',
            'CountryOnOFF',
            'EnableFullMediaView',
            'OpenForSEO',
            'SEOTitle',
            'SEOContent',
            'SEOKeyword'
        )


class CountryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryEvent
        fields = (
            'SortId',
            'CountryEventId',
            'Identification',
            'CountryType',
            'ContinentId',
            'CountryEventName',
            'CountryCode',
            'CountryNumericCode',
            'CountryTag',
            'TelephoneCode',
            'Description',
            'Logo',
            'InfoImage',
            'BannerImage',
            'StartDate',
            'EndDate',
            'MatchingCategoriesToAd',
            'GeneralInfo',
            'AvailableVertical',
            'CountryOnOFF',
            'EnableFullMediaView',
            'OpenForSEO',
            'SEOTitle',
            'SEOContent',
            'SEOKeyword'
        )


class UploadCountryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryEvent
        fields = (
            'SortId',
            'CountryEventId',
            'CountryEventName',
            'Logo',
            'InfoImage',
            'BannerImage'
        )


class CityRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityRegion
        fields = (
            'SortId',
            'CityId',
            'CountryId',
            'CityRegionName',
        )


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'SortId',
            'LocationId',
            'CityId',
            'LocationName',
        )


class SaveNearByAdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NearByAdvantage
        fields = (
            # 'SortId',
            'NearByAdvantageId',
            'NearByAdvantage',
        )


class NearByAdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NearByAdvantage
        fields = (
            # 'SortId',
            'NearByAdvantageId',
            'NearByAdvantage',
            'NearByAdvantageIcon',
        )


class UploadNearByAdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NearByAdvantage
        fields = (
            'SortId',
            'NearByAdvantageId',
            'NearByAdvantage',
            'NearByAdvantageIcon',
        )


class AdunitPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdunitPosition
        fields = (
            'SortId',
            'AdunitPositionId',
            'AdunitPosition',
            'VerticalId'
        )


class AdunitSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdunitSize
        fields = (
            'SortId',
            'AdunitSizeId',
            'AdunitSize',
            'VerticalId'
        )


class MediaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaCategory
        fields = (
            'SortId',
            'MediaCategoryId',
            'MediaCategory',
            'VerticalId'
        )


class AdFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdFormat
        fields = (
            'SortId',
            'AdFormatId',
            'AdFormat',
            'VerticalId'
        )


class BrandCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandCategory
        fields = (
            'SortId',
            'BrandCategoryId',
            'BrandCategory'
        )


class CampaignObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignObjective
        fields = (
            'SortId',
            'CampaignObjectiveId',
            'Identification',
            'CampaignObjective'
        )


class HelpRequiredForSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpRequiredFor
        fields = (
            'SortId',
            'HelpRequiredForId',
            'HelpRequiredFor',
            'HelpForUser'
        )


class SaveMeetingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRequest
        fields = (
            # 'SortId',
            'MeetingRequestId',
            'UserId',
            'UserTypeId',
            'HelpRequiredFor',
            'Message',
            'CreatedDate',
            'Status'
        )


class AdUnitSpecificCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdUnitSpecificCategory
        fields = (
            # 'SortId',
            'AdUnitSpecificCategoryId',
            'Identification',
            'VerticalId',
            'AdUnitSpecificCategory',
            'AdUnitSpecificCategoryIcon',
            'OrderNo'
        )


class SaveAdUnitSpecificCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdUnitSpecificCategory
        fields = (
            # 'SortId',
            'AdUnitSpecificCategoryId',
            'Identification',
            'VerticalId',
            'AdUnitSpecificCategory',
            'OrderNo'
        )

class UploadAdUnitSpecificCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdUnitSpecificCategory
        fields = (
            # 'SortId',
            'AdUnitSpecificCategoryId',
            'AdUnitSpecificCategory',
            'AdUnitSpecificCategoryIcon',
        )

class HighlyRecommendedMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighlyRecommendedMedia
        fields = (
            # 'SortId',
            'HighlyRecommendedMediaId',
            'AudienceId',
            'CountryId',
            'TypeId',
            'Type',
            'AdUnit',
            'Media',
            'SEOTitle',
            'SEOContent',
            'SEOKeyword',
            'OrderNo'
        )


class RecommendationBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationBanner
        fields = (
            # 'SortId',
            'RecommendationBannerId',
            'AudienceId',
            'CountryId',
            'Heading',
            'Description',
            'Caption',
            'BannerType',
            'BannerImage',
            'BannerImageForMobile',
            'VideoLink',
            'BannerMediaType',
            'AdUnit',
            'PageLink',
            'OrderNo',
            'SEOTitle',
            'SEOContent',
            'SEOKeyword'
        )


class SaveRecommendationBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationBanner
        fields = (
            # 'SortId',
            'RecommendationBannerId',
            'AudienceId',
            'CountryId',
            'Heading',
            'Description',
            'Caption',
            'VideoLink',
            'BannerType',
            'BannerMediaType',
            'AdUnit',
            'PageLink',
            'OrderNo',
            'SEOTitle',
            'SEOContent',
            'SEOKeyword'
        )


class UploadRecommendationBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationBanner
        fields = (
            # 'SortId',
            'RecommendationBannerId',
            'AudienceId',
            'BannerImage',
            'BannerImageForMobile'
        )


class SiteBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteBanner
        fields = (
            # 'SortId',
            'SiteBannerId',
            'AudienceId',
            'CountryId',
            'CategoryId',
            'CategoryType',
            'Heading',
            'Description',
            'Caption',
            'BannerType',
            'BannerImage',
            'BannerImageForMobile',
            'VideoLink',
            'BannerMediaType',
            'AdUnit',
            'PageLink',
            'OrderNo',
            'SEOTitle',
            'SEOContent',
            'SEOKeyword'
        )


class SaveSiteBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteBanner
        fields = (
            # 'SortId',
            'SiteBannerId',
            'AudienceId',
            'CountryId',
            'CategoryId',
            'CategoryType',
            'Heading',
            'Description',
            'Caption',
            'VideoLink',
            'BannerType',
            'BannerMediaType',
            'AdUnit',
            'PageLink',
            'OrderNo',
            'SEOTitle',
            'SEOContent',
            'SEOKeyword'
        )


class UploadSiteBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteBanner
        fields = (
            # 'SortId',
            'SiteBannerId',
            'AudienceId',
            'BannerImage',
            'BannerImageForMobile'
        )


class AdBuzzCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdBuzzCategory
        fields = (
            'SortId',
            'AdBuzzCategoryId',
            'AdBuzzCategory',
            'OrderNo'
        )

class CampaignUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignUnit
        fields = (
            'SortId',
            'CampaignUnitId',
            'CampaignUnit',
            'UnitType',
            'CampaignUnitIcon'
        )

class SaveCampaignUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignUnit
        fields = (
            'CampaignUnitId',
            'CampaignUnit',
            'UnitType',
        )

class UploadCampaignUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignUnit
        fields = (
            'CampaignUnitId',
            'CampaignUnitIcon'
        )

class SiteMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteMenu
        fields = (
            'SortId',
            'SiteMenuId',
            'SiteMenu',
            'LinkType',
            'Link',
            'OrderNo'
        )