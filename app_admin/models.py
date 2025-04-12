from datetime import datetime
import uuid
from django.db import models

# Create your models here.


class Continent(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    ContinentId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    Continent = models.CharField(blank=True, null=True, max_length=300)
    ContinentOnOFF = models.IntegerField(default=1)
    OrderNo = models.IntegerField(blank=True, null=True, default=0)


class CountryEvent(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    CountryEventId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    Identification = models.IntegerField(default=1000)
    ContinentId = models.CharField(blank=True, null=True, max_length=50)
    CountryType = models.CharField(blank=True, null=True, max_length=50)
    CountryEventName = models.CharField(blank=True, null=True, max_length=300)
    CountryNumericCode = models.CharField(blank=True, null=True, max_length=10)
    CountryCode = models.CharField(blank=True, null=True, max_length=10)
    TelephoneCode = models.CharField(blank=True, null=True, max_length=10)
    CountryTag = models.TextField(blank=True, null=True,)
    Description = models.TextField(blank=True, null=True,)
    GeneralInfo = models.TextField(blank=True, null=True,)
    Logo = models.FileField(blank=True, null=True, upload_to='CountryEvent')
    InfoImage = models.FileField(
        blank=True, null=True, upload_to='CountryEvent')
    BannerImage = models.FileField(
        blank=True, null=True, upload_to='CountryEvent')
    StartDate = models.CharField(blank=True, null=True, max_length=400)
    EndDate = models.CharField(blank=True, null=True, max_length=400)
    MatchingCategoriesToAd = models.TextField(blank=True, null=True)
    AvailableVertical = models.TextField(blank=True, null=True)
    CountryOnOFF = models.IntegerField(default=1)
    OpenForSEO = models.BooleanField(default=False)
    SEOTitle = models.TextField(blank=True, null=True)
    SEOContent = models.TextField(blank=True, null=True)
    SEOKeyword = models.TextField(blank=True, null=True)
    EnableFullMediaView = models.BooleanField(default=False)


class CityRegion(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    CityId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    CountryId = models.CharField(max_length=50)
    CityRegionName = models.CharField(max_length=300)


class Location(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    LocationId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    CityId = models.CharField(max_length=50)
    LocationName = models.CharField(max_length=300)


class StaffRegister(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    StaffId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    EmailId = models.CharField(max_length=300)
    Name = models.CharField(max_length=300)
    UserGroup = models.CharField(max_length=50)


class VerticalType(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    VerticalTypeId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    VerticalId = models.CharField(max_length=50)
    VerticalType = models.CharField(max_length=300)


class Language(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    LanguageId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    Language = models.CharField(max_length=300)

class AdBuzzTagging(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    AdBuzzTaggingId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    AdBuzzTagging = models.CharField(max_length=300)


class EstimatedReach(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    EstimatedReachId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    EstimatedReach = models.CharField(max_length=300)
    ReachFrom = models.IntegerField(default=0)
    ReachTo = models.IntegerField(default=0)
    AverageReach = models.CharField(max_length=50, blank=True, null=True)


class LocationType(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    LocationTypeId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    LocationType = models.CharField(max_length=300)


class NearByAdvantage(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    NearByAdvantageId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    NearByAdvantage = models.CharField(max_length=300)
    NearByAdvantageIcon = models.FileField(
        blank=True, null=True, upload_to='NearByAdvantage')


def uploadMatachingCategory(instance, fileName):
    return '/'.join(['MatachingCategory', str(instance.MatchingCategory), fileName])


class MatchingCategory(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    MatchingCategoryId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    Identification = models.IntegerField(default=1000)
    MatchingCategory = models.CharField(max_length=300)
    CategoryIcon = models.FileField(
        blank=True, null=True, upload_to='MatachingCategory')
    Enable = models.BooleanField(default=False)


class AgeGroup(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    AgeGroupId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    AgeGroup = models.CharField(max_length=300)
    AgeGroupIcon = models.FileField(
        blank=True, null=True, upload_to='AgeGroup')


class GenderGroup(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    GenderGroupId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    GenderGroup = models.CharField(max_length=300)
    GenderGroupIcon = models.FileField(
        blank=True, null=True, upload_to='GenderGroup')


def uploadIncomeGroup(instance, fileName):
    return '/'.join(['IncomeGroup', str(instance.MatchingCategory), fileName])


class IncomeGroup(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    IncomeGroupId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    IncomeGroup = models.CharField(max_length=300)
    IncomeGroupIcon = models.FileField(
        blank=True, null=True, upload_to='IncomeGroup')


class NationalityCommunity(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    NationalityCommunityId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    NationalityCommunity = models.CharField(max_length=300)


class AdunitPosition(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    AdunitPositionId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    AdunitPosition = models.CharField(max_length=300)
    VerticalId = models.CharField(max_length=300)


class AdunitSize(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    AdunitSizeId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    AdunitSize = models.CharField(max_length=300)
    VerticalId = models.CharField(max_length=300)


class MediaCategory(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    MediaCategoryId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    MediaCategory = models.CharField(max_length=300)
    VerticalId = models.CharField(max_length=300)


class AdFormat(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    AdFormatId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    AdFormat = models.CharField(max_length=300)
    VerticalId = models.CharField(max_length=300)


class BrandCategory(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    BrandCategoryId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    BrandCategory = models.CharField(max_length=300)


class CampaignObjective(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    CampaignObjectiveId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    Identification = models.IntegerField(default=1000)
    CampaignObjective = models.CharField(max_length=300)


class HelpRequiredFor(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    HelpRequiredForId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    HelpRequiredFor = models.CharField(max_length=300)
    HelpForUser = models.CharField(max_length=50)


class MeetingRequest(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    MeetingRequestId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    UserId = models.CharField(max_length=50, blank=True, null=True)
    UserTypeId = models.CharField(max_length=50, blank=True, null=True)
    HelpRequiredFor = models.TextField(blank=True, null=True)
    Message = models.TextField(blank=True, null=True)
    CreatedDate = models.CharField(max_length=200, blank=True, null=True)
    Status = models.IntegerField(blank=True, null=True)


class AdUnitSpecificCategory(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    AdUnitSpecificCategoryId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    Identification = models.IntegerField(default=1000)
    VerticalId = models.CharField(max_length=50, blank=True, null=True)
    AdUnitSpecificCategory = models.CharField(max_length=200)
    AdUnitSpecificCategoryIcon = models.FileField(
        blank=True, null=True, upload_to='AdUnitSpecificCategoryIcon')
    OrderNo = models.IntegerField(blank=True, null=True, default=0)


class HighlyRecommendedMedia(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    HighlyRecommendedMediaId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    CountryId = models.CharField(max_length=50, blank=True, null=True)
    AudienceId = models.CharField(max_length=50, blank=True, null=True)
    # verticalid or specific category id
    TypeId = models.CharField(max_length=50, blank=True, null=True)
    # vertical or specific category
    Type = models.CharField(max_length=300, blank=True, null=True)
    AdUnit = models.TextField(blank=True, null=True)
    Media = models.TextField(blank=True, null=True)
    SEOTitle = models.TextField(blank=True, null=True)
    SEOContent = models.TextField(blank=True, null=True)
    SEOKeyword = models.TextField(blank=True, null=True)
    OrderNo = models.IntegerField(default=0)


class RecommendationBanner(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    RecommendationBannerId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    CountryId = models.CharField(max_length=50, blank=True, null=True)
    AudienceId = models.CharField(max_length=50, blank=True, null=True)
    Heading = models.CharField(max_length=300, blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    Caption = models.CharField(max_length=300, blank=True, null=True)
    BannerType = models.CharField(default="Normal",
                                  max_length=50, blank=True, null=True)
    # Normal/Full
    BannerImage = models.FileField(
        blank=True, null=True, upload_to='listing_banner')
    BannerImageForMobile = models.FileField(
        blank=True, null=True, upload_to='listing_banner')
    VideoLink = models.TextField(blank=True, null=True)
    BannerMediaType = models.CharField(
        max_length=50, blank=True, null=True)  # Video/Image
    AdUnit = models.CharField(max_length=50, blank=True, null=True)
    PageLink = models.TextField(blank=True, null=True)
    OrderNo = models.IntegerField(blank=True, null=True, default=0)
    SEOTitle = models.TextField(blank=True, null=True)
    SEOContent = models.TextField(blank=True, null=True)
    SEOKeyword = models.TextField(blank=True, null=True)

class SiteBanner(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    SiteBannerId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    CountryId = models.CharField(max_length=50, blank=True, null=True)
    AudienceId = models.CharField(max_length=50, blank=True, null=True)
    CategoryId = models.CharField(max_length=50, blank=True, null=True)
    CategoryType = models.CharField(max_length=50, blank=True, null=True)
    Heading = models.CharField(max_length=300, blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    Caption = models.CharField(max_length=300, blank=True, null=True)
    BannerType = models.CharField(default="Normal",
                                  max_length=50, blank=True, null=True)
    # Normal/Full
    BannerImage = models.FileField(
        blank=True, null=True, upload_to='listing_banner/view_all')
    BannerImageForMobile = models.FileField(
        blank=True, null=True, upload_to='listing_banner/view_all')
    VideoLink = models.TextField(blank=True, null=True)
    BannerMediaType = models.CharField(
        max_length=50, blank=True, null=True)  # Video/Image
    AdUnit = models.CharField(max_length=50, blank=True, null=True)
    PageLink = models.TextField(blank=True, null=True)
    OrderNo = models.IntegerField(blank=True, null=True, default=0)
    SEOTitle = models.TextField(blank=True, null=True)
    SEOContent = models.TextField(blank=True, null=True)
    SEOKeyword = models.TextField(blank=True, null=True)


class AdBuzzCategory(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    AdBuzzCategoryId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    AdBuzzCategory = models.CharField(max_length=300, blank=True, null=True)
    OrderNo = models.IntegerField(blank=True, null=True, default=0)


class CampaignUnit(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    CampaignUnitId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    CampaignUnit = models.CharField(max_length=300)
    UnitType = models.CharField(
        max_length=300, blank=True, null=True, default='Count')
    CampaignUnitIcon = models.FileField(
        blank=True, null=True, upload_to='CampaignUnit')


class SiteMenu(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    SiteMenuId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    SiteMenu = models.CharField(max_length=300, blank=True, null=True)
    LinkType = models.CharField(max_length=300, blank=True, null=True)
    Link = models.TextField(blank=True, null=True)
    OrderNo = models.IntegerField(default=0,blank=True, null=True)
