from datetime import datetime
import uuid
from django.db import models

# Create your models here.


class Media(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    Identification = models.IntegerField(default=1000)
    MediaId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    VerticalType = models.CharField(blank=True, null=True, max_length=50)
    MediaName = models.CharField(blank=True, null=True, max_length=300)
    Category = models.CharField(blank=True, null=True, max_length=50)
    PrimaryLanguage = models.TextField(blank=True, null=True)
    TimeZone = models.CharField(blank=True, null=True, max_length=50)
    MediaManagedBy = models.CharField(blank=True, null=True, max_length=300)
    WebsiteLink = models.CharField(blank=True, null=True, max_length=300)
    WebStatsOnOff = models.CharField(blank=True, null=True, max_length=300)
    EventVenue = models.CharField(blank=True, null=True, max_length=300)
    PublisherId = models.CharField(blank=True, null=True, max_length=50)
    CountryEvent = models.TextField(blank=True, null=True)
    ContactPerson = models.TextField(blank=True, null=True)
    CityRegion = models.TextField(blank=True, null=True)
    Language = models.TextField(blank=True, null=True)
    EstimateReached = models.CharField(blank=True, null=True, max_length=50)
    BenefitsOfAdvertising = models.TextField(blank=True, null=True)
    PromoVideoLink = models.CharField(blank=True, null=True, max_length=300)
    MediaKit = models.FileField(
        blank=True, null=True, upload_to='vertical/Media/mediakit')
    MapLink = models.TextField(blank=True, null=True)
    Latitude = models.CharField(blank=True, null=True, max_length=300)
    Longitude = models.CharField(blank=True, null=True, max_length=300)
    IsHyperlocal = models.CharField(blank=True, null=True, max_length=300)
    Availability = models.TextField(blank=True, null=True)
    MediaCategory = models.CharField(blank=True, null=True, max_length=300)
    MediaImage = models.FileField(
        blank=True, null=True, upload_to='vertical/Media/image')
    Status = models.IntegerField(blank=True, null=True)
    ViewsCount = models.IntegerField(blank=True, null=True)
    ModifiedDate = models.DateTimeField(blank=True, null=True)
    RecommendedMedia = models.TextField(blank=True, null=True)
    ShowOnOff = models.IntegerField(blank=True, null=True)
    ViewOnlyMediaStore = models.IntegerField(blank=True, null=True)
    SEOMetaTitle = models.TextField(blank=True, null=True)
    SEOMetaDescription = models.TextField(blank=True, null=True)
    SEOMetaKeyword = models.TextField(blank=True, null=True)
    CountryEventJSON = models.JSONField(null=True, blank=True)
    CityRegionJSON = models.JSONField(null=True, blank=True)
    LanguageJSON = models.JSONField(null=True, blank=True)
    SEOMetaKeywordJSON = models.JSONField(null=True, blank=True)

    BenefitsOfAdvertisingNonHTML = models.TextField(blank=True, null=True)
    # SEOURL = models.TextField(blank=True, null=True)
    # SEOContent = models.TextField(blank=True, null=True)
    # SEOImage = models.FileField(
    #     blank=True, null=True, upload_to='vertical/Media/SEO')
    # SEOVideoURL = models.CharField(blank=True, null=True, max_length=300)


class MediaRegionReach(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    MediaRegionReachId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    MediaId = models.CharField(blank=True, null=True, max_length=50)
    CityRegionId = models.CharField(blank=True, null=True, max_length=50)
    EstimateReach = models.CharField(blank=True, null=True, max_length=50)


class MediaAdType(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    Identification = models.IntegerField(default=1000)
    MediaAdTypeId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    MediaId = models.CharField(blank=True, null=True, max_length=300)
    Size = models.CharField(blank=True, null=True, max_length=300)
    OutdoorSize = models.CharField(blank=True, null=True, max_length=300)
    CreativeSize = models.CharField(blank=True, null=True, max_length=300)
    AdFormat = models.CharField(blank=True, null=True, max_length=300)
    NumberOfSpots = models.CharField(blank=True, null=True, max_length=300)
    SpecificCategory = models.CharField(blank=True, null=True, max_length=50)
    PromoAudio = models.FileField(
        blank=True, null=True, upload_to='vertical/Media/audio')
    ProgramStartTime = models.CharField(blank=True, null=True, max_length=300)
    ProgramEndTime = models.CharField(blank=True, null=True, max_length=300)
    OrderUnit = models.CharField(blank=True, null=True, max_length=300)
    UnitType = models.CharField(blank=True, null=True, max_length=300)
    OrderingQuantity = models.CharField(blank=True, null=True, max_length=300)
    CreativesRequired = models.CharField(blank=True, null=True, max_length=300)
    Position = models.CharField(blank=True, null=True, max_length=300)
    DigitalPosition = models.CharField(blank=True, null=True, max_length=300)
    MediaAdType = models.CharField(blank=True, null=True, max_length=300)
    SiteName = models.CharField(blank=True, null=True, max_length=300)
    LocationType = models.CharField(blank=True, null=True, max_length=300)
    VerticalTypeId = models.CharField(blank=True, null=True, max_length=300)
    NoOfScreen = models.CharField(blank=True, null=True, max_length=300)
    MediaAdUnitDescription = models.TextField(blank=True, null=True)
    IsDigital = models.CharField(blank=True, null=True, max_length=300)
    SingleRotationTime = models.CharField(
        blank=True, null=True, max_length=300)
    DurationOfCreative = models.CharField(
        blank=True, null=True, max_length=300)
    Availability = models.TextField(blank=True, null=True)
    PackageName = models.CharField(blank=True, null=True, max_length=300)
    PackageType = models.CharField(blank=True, null=True, max_length=300)
    StartDate = models.CharField(blank=True, null=True, max_length=300)
    EndDate = models.CharField(blank=True, null=True, max_length=300)
    NoOfDays = models.CharField(blank=True, null=True, max_length=300)
    PromoVideoLink = models.CharField(blank=True, null=True, max_length=300)
    Currency = models.CharField(blank=True, null=True, max_length=30)
    MonthlyRentalRate = models.CharField(blank=True, null=True, max_length=300)
    Discount = models.CharField(blank=True, null=True, max_length=300)
    NetCostBeforeTax = models.CharField(blank=True, null=True, max_length=300)
    ProductionCost = models.CharField(blank=True, null=True, max_length=300)
    Tax = models.CharField(blank=True, null=True, max_length=300)
    NetCost = models.CharField(blank=True, null=True, max_length=300)
    RateValidaty = models.CharField(blank=True, null=True, max_length=300)
    CostPerThousandDisplay = models.CharField(
        blank=True, null=True, max_length=10)
    CostPerThousand = models.CharField(blank=True, null=True, max_length=300)
    AdUnitCategory = models.CharField(blank=True, null=True, max_length=300)
    AdTypeMediaKit = models.FileField(
        blank=True, null=True, upload_to='vertical/Media/mediakit')
    AdTypeEstimateReached = models.TextField(blank=True, null=True)
    NearByAdvantages = models.TextField(blank=True, null=True)
    MatchingCategories = models.TextField(blank=True, null=True)
    AgeGroup = models.TextField(blank=True, null=True)
    GenderGroup = models.TextField(blank=True, null=True)
    IncomeGroup = models.TextField(blank=True, null=True)
    NationalityCommunity = models.TextField(blank=True, null=True)
    RunAsOffer = models.CharField(blank=True, null=True, max_length=300)
    IsLocalTaxApplied = models.CharField(blank=True, null=True, max_length=300)
    IsNeedApproval = models.CharField(blank=True, null=True, max_length=300)
    NoOfDaysRequired = models.CharField(blank=True, null=True, max_length=300)
    MediaAdTypeImage = models.CharField(blank=True, null=True, max_length=300)
    TermsAndConditions = models.TextField(blank=True, null=True)
    ThumbnailImage = models.FileField(
        blank=True, null=True, upload_to='vertical/Media/image')
    RateDisplay = models.CharField(blank=True, null=True, max_length=10)
    Status = models.IntegerField(blank=True, null=True)
    PriceRangeNote= models.TextField(blank=True, null=True)
    ShowOnOff = models.IntegerField(blank=True, null=True)
    AvailabilityJSON = models.JSONField(blank=True, null=True)
    NearByAdvantagesJSON = models.JSONField(blank=True, null=True)
    MatchingCategoriesJSON = models.JSONField(blank=True, null=True)
    AgeGroupJSON = models.JSONField(blank=True, null=True)
    GenderGroupJSON = models.JSONField(blank=True, null=True)
    IncomeGroupJSON = models.JSONField(blank=True, null=True)

    MediaAdUnitDescriptionNonHTML = models.TextField(blank=True, null=True)
    TermsAndConditionsNonHTML = models.TextField(blank=True, null=True)


class MediaAdTypeImage(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    MediaAdTypeImageId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    MediaAdTypeId = models.CharField(blank=True, null=True, max_length=300)
    MediaAdTypeImage = models.FileField(
        blank=True, null=True, upload_to='vertical/Media/image')
    OrderNo = models.IntegerField(default=0, blank=True, null=True)


class MediaView(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    Identification = models.IntegerField(default=1000)
    MediaId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    VerticalType = models.CharField(blank=True, null=True, max_length=50)
    MediaName = models.CharField(blank=True, null=True, max_length=300)
    Category = models.CharField(blank=True, null=True, max_length=50)
    PrimaryLanguage = models.TextField(blank=True, null=True)
    TimeZone = models.CharField(blank=True, null=True, max_length=50)
    MediaManagedBy = models.CharField(blank=True, null=True, max_length=300)
    WebsiteLink = models.CharField(blank=True, null=True, max_length=300)
    WebStatsOnOff = models.CharField(blank=True, null=True, max_length=300)
    EventVenue = models.CharField(blank=True, null=True, max_length=300)
    PublisherId = models.CharField(blank=True, null=True, max_length=50)
    CountryEvent = models.TextField(blank=True, null=True)
    ContactPerson = models.TextField(blank=True, null=True)
    CityRegion = models.TextField(blank=True, null=True)
    Language = models.TextField(blank=True, null=True)
    EstimateReached = models.CharField(blank=True, null=True, max_length=50)
    BenefitsOfAdvertising = models.TextField(blank=True, null=True)
    PromoVideoLink = models.CharField(blank=True, null=True, max_length=300)
    MediaKit = models.FileField(
        blank=True, null=True, upload_to='vertical/Media/mediakit')
    MapLink = models.TextField(blank=True, null=True)
    Latitude = models.CharField(blank=True, null=True, max_length=300)
    Longitude = models.CharField(blank=True, null=True, max_length=300)
    IsHyperlocal = models.CharField(blank=True, null=True, max_length=300)
    Availability = models.TextField(blank=True, null=True)
    MediaCategory = models.CharField(blank=True, null=True, max_length=300)
    MediaImage = models.FileField(
        blank=True, null=True, upload_to='vertical/Media/image')
    Status = models.IntegerField(blank=True, null=True)
    ViewsCount = models.IntegerField(blank=True, null=True)
    ModifiedDate = models.DateTimeField(blank=True, null=True)
    RecommendedMedia = models.TextField(blank=True, null=True)
    ShowOnOff = models.IntegerField(blank=True, null=True)
    ViewOnlyMediaStore = models.IntegerField(blank=True, null=True)
    SEOMetaTitle = models.TextField(blank=True, null=True)
    SEOMetaDescription = models.TextField(blank=True, null=True)
    SEOMetaKeyword = models.TextField(blank=True, null=True)
    CountryEventJSON = models.JSONField(null=True, blank=True)
    CityRegionJSON = models.JSONField(null=True, blank=True)
    LanguageJSON = models.JSONField(null=True, blank=True)
    SEOMetaKeywordJSON = models.JSONField(null=True, blank=True)
    BenefitsOfAdvertisingNonHTML = models.TextField(blank=True, null=True)
    VerticalTypeName = models.CharField(blank=True, null=True, max_length=300)
    CategoryName = models.CharField(blank=True, null=True, max_length=300)
    TimeZoneName = models.CharField(blank=True, null=True, max_length=300)
    LanguageName = models.CharField(blank=True, null=True, max_length=300)
    PublisherName = models.CharField(blank=True, null=True, max_length=300)
    EstimatedReachName = models.CharField(
        blank=True, null=True, max_length=300)
    AdUnitCategoryName = models.CharField(
        blank=True, null=True, max_length=300)

    class Meta:
        managed = False
        db_table = 'MediaView'

# CREATE VIEW MediaView as SELECT
#     app_vertical_media_media.*,
#     app_default_vertical.VerticalName as VerticalTypeName,
#     app_admin_mediacategory.MediaCategory as CategoryName,
#     app_default_timezone.TimeZone as TimeZoneName,
#     app_admin_language.Language as LanguageName,
#     app_publisher_publisherregister.MediaName as PublisherName,
# app_admin_estimatedreach.EstimatedReach as EstimatedReachName,
# app_default_adunitcategory.AdUnitCategory as AdUnitCategoryName
# FROM
#     app_vertical_media_media
# LEFT JOIN
#     app_default_vertical
# ON
#     app_vertical_media_media.VerticalType = app_default_vertical.VerticalId
# LEFT JOIN
#     app_admin_mediacategory
# ON
#     app_vertical_media_media.Category = app_admin_mediacategory.MediaCategoryId
# LEFT JOIN
#     app_default_timezone
# ON
#     app_vertical_media_media.TimeZone = app_default_timezone.TimeZoneId
# LEFT JOIN
#     app_admin_language
# ON
#     app_vertical_media_media.PrimaryLanguage = app_admin_language.LanguageId
# LEFT JOIN
#     app_publisher_publisherregister
# ON
#     app_vertical_media_media.PublisherId = app_publisher_publisherregister.PublisherId
# LEFT JOIN
#     app_admin_estimatedreach
# ON
#    app_vertical_media_media.EstimateReached = app_admin_estimatedreach.EstimatedReachId
# LEFT JOIN
#     app_default_adunitcategory
# ON
#     app_vertical_media_media.MediaCategory = app_default_adunitcategory.AdUnitCategoryId


class MediaAdTypeView(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    Identification = models.IntegerField(default=1000)
    MediaAdTypeId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    MediaId = models.CharField(blank=True, null=True, max_length=300)
    Size = models.CharField(blank=True, null=True, max_length=300)
    OutdoorSize = models.CharField(blank=True, null=True, max_length=300)
    CreativeSize = models.CharField(blank=True, null=True, max_length=300)
    AdFormat = models.CharField(blank=True, null=True, max_length=300)
    NumberOfSpots = models.CharField(blank=True, null=True, max_length=300)
    SpecificCategory = models.CharField(blank=True, null=True, max_length=50)
    PromoAudio = models.FileField(
        blank=True, null=True, upload_to='vertical/Media/audio')
    ProgramStartTime = models.CharField(blank=True, null=True, max_length=300)
    ProgramEndTime = models.CharField(blank=True, null=True, max_length=300)
    OrderUnit = models.CharField(blank=True, null=True, max_length=300)
    UnitType = models.CharField(blank=True, null=True, max_length=300)
    OrderingQuantity = models.CharField(blank=True, null=True, max_length=300)
    CreativesRequired = models.CharField(blank=True, null=True, max_length=300)
    Position = models.CharField(blank=True, null=True, max_length=300)
    DigitalPosition = models.CharField(blank=True, null=True, max_length=300)
    MediaAdType = models.CharField(blank=True, null=True, max_length=300)
    SiteName = models.CharField(blank=True, null=True, max_length=300)
    LocationType = models.CharField(blank=True, null=True, max_length=300)
    VerticalTypeId = models.CharField(blank=True, null=True, max_length=300)
    NoOfScreen = models.CharField(blank=True, null=True, max_length=300)
    MediaAdUnitDescription = models.TextField(blank=True, null=True)
    IsDigital = models.CharField(blank=True, null=True, max_length=300)
    SingleRotationTime = models.CharField(
        blank=True, null=True, max_length=300)
    DurationOfCreative = models.CharField(
        blank=True, null=True, max_length=300)
    Availability = models.TextField(blank=True, null=True)
    PackageName = models.CharField(blank=True, null=True, max_length=300)
    PackageType = models.CharField(blank=True, null=True, max_length=300)
    StartDate = models.CharField(blank=True, null=True, max_length=300)
    EndDate = models.CharField(blank=True, null=True, max_length=300)
    NoOfDays = models.CharField(blank=True, null=True, max_length=300)
    PromoVideoLink = models.CharField(blank=True, null=True, max_length=300)
    Currency = models.CharField(blank=True, null=True, max_length=30)
    MonthlyRentalRate = models.CharField(blank=True, null=True, max_length=300)
    Discount = models.CharField(blank=True, null=True, max_length=300)
    NetCostBeforeTax = models.CharField(blank=True, null=True, max_length=300)
    ProductionCost = models.CharField(blank=True, null=True, max_length=300)
    Tax = models.CharField(blank=True, null=True, max_length=300)
    NetCost = models.CharField(blank=True, null=True, max_length=300)
    RateValidaty = models.CharField(blank=True, null=True, max_length=300)
    CostPerThousandDisplay = models.CharField(
        blank=True, null=True, max_length=10)
    CostPerThousand = models.CharField(blank=True, null=True, max_length=300)
    AdUnitCategory = models.CharField(blank=True, null=True, max_length=300)
    AdTypeMediaKit = models.FileField(
        blank=True, null=True, upload_to='vertical/Media/mediakit')
    AdTypeEstimateReached = models.TextField(blank=True, null=True)
    NearByAdvantages = models.TextField(blank=True, null=True)
    MatchingCategories = models.TextField(blank=True, null=True)
    AgeGroup = models.TextField(blank=True, null=True)
    GenderGroup = models.TextField(blank=True, null=True)
    IncomeGroup = models.TextField(blank=True, null=True)
    NationalityCommunity = models.TextField(blank=True, null=True)
    RunAsOffer = models.CharField(blank=True, null=True, max_length=300)
    IsLocalTaxApplied = models.CharField(blank=True, null=True, max_length=300)
    IsNeedApproval = models.CharField(blank=True, null=True, max_length=300)
    NoOfDaysRequired = models.CharField(blank=True, null=True, max_length=300)
    MediaAdTypeImage = models.CharField(blank=True, null=True, max_length=300)
    TermsAndConditions = models.TextField(blank=True, null=True)
    ThumbnailImage = models.FileField(
        blank=True, null=True, upload_to='vertical/Media/image')
    RateDisplay = models.CharField(blank=True, null=True, max_length=10)
    Status = models.IntegerField(blank=True, null=True)
    ShowOnOff = models.IntegerField(blank=True, null=True)
    AvailabilityJSON = models.JSONField(blank=True, null=True)
    NearByAdvantagesJSON = models.JSONField(blank=True, null=True)
    MatchingCategoriesJSON = models.JSONField(blank=True, null=True)
    AgeGroupJSON = models.JSONField(blank=True, null=True)
    GenderGroupJSON = models.JSONField(blank=True, null=True)
    IncomeGroupJSON = models.JSONField(blank=True, null=True)
    MediaAdUnitDescriptionNonHTML = models.TextField(blank=True, null=True)
    TermsAndConditionsNonHTML = models.TextField(blank=True, null=True)
    MediaName = models.CharField(blank=True, null=True, max_length=300)
    SizeName = models.CharField(blank=True, null=True, max_length=300)
    AdFormatName = models.CharField(blank=True, null=True, max_length=300)
    AdunitPosition = models.CharField(blank=True, null=True, max_length=300)
    LocationTypeName = models.CharField(blank=True, null=True, max_length=300)
    VerticalTypeName = models.CharField(blank=True, null=True, max_length=300)
    AdUnitCategoryIdName = models.CharField(
        blank=True, null=True, max_length=300)
    EstimatedReachName = models.CharField(
        blank=True, null=True, max_length=300)
    AdUnitSpecificCategoryName = models.CharField(
        blank=True, null=True, max_length=300)

    class Meta:
        managed = False
        db_table = 'MediaAdTypeView'


class MediaAdTypeWithMediaView(models.Model):
    MediaAdTypeId = models.CharField(blank=True, null=True, max_length=50)
    MediaAdType = models.CharField(blank=True, null=True, max_length=300)
    PackageName = models.CharField(blank=True, null=True, max_length=300)
    SiteName = models.CharField(blank=True, null=True, max_length=300)
    MediaName = models.CharField(blank=True, null=True, max_length=300)
    ThumbnailImage = models.CharField(blank=True, null=True, max_length=300)
    MediaAdUnitDescriptionNonHTML = models.TextField(blank=True, null=True)
    VerticalTypeName = models.CharField(blank=True, null=True, max_length=300)
    VerticalType = models.CharField(blank=True, null=True, max_length=50)
    MediaId = models.CharField(blank=True, null=True, max_length=50)
    PriceRangeNote= models.TextField(blank=True, null=True)
    CountryEventJSON = models.TextField(blank=True, null=True)
    CityRegionJSON = models.TextField(blank=True, null=True)
    LanguageJSON = models.TextField(blank=True, null=True)
    LanguageName = models.CharField(blank=True, null=True, max_length=300)
    EstimatedReachName = models.CharField(blank=True, null=True, max_length=300)
    MediaImage = models.CharField(blank=True, null=True, max_length=100)
    MediaCategory = models.CharField(blank=True, null=True, max_length=300)
    MediaManagedBy = models.CharField(blank=True, null=True, max_length=300)
    MatchingCategoriesJSON = models.TextField(blank=True, null=True)
    AdUnitSpecificCategoryName = models.CharField(blank=True, null=True, max_length=300)
    RunAsOffer = models.CharField(blank=True, null=True, max_length=300)
    NetCost = models.CharField(blank=True, null=True, max_length=300)
    Currency = models.CharField(blank=True, null=True, max_length=30)
    LocationType = models.CharField(blank=True, null=True, max_length=300)

class Meta:
    managed = False
    db_table = 'MediaAdTypeWithMediaView'
# CREATE VIEW MediaAdTypeView as SELECT
#     app_vertical_media_mediaadtype.*,
#     app_vertical_media_media.MediaName as MediaName,
#     app_admin_adunitsize.AdunitSize as SizeName,
#      app_admin_adformat.AdFormat as AdFormatName,
#      app_admin_adunitposition.AdunitPosition as AdunitPosition,
#      app_admin_locationtype.LocationType  as LocationTypeName,
#      app_admin_verticaltype.VerticalType as VerticalTypeName,
#      app_default_adunitcategory.AdUnitCategory as AdUnitCategoryIdName,
#       app_admin_estimatedreach.EstimatedReach as EstimatedReachName,
#       app_admin_adunitspecificcategory.AdUnitSpecificCategory as AdUnitSpecificCategoryName
# FROM
#     app_vertical_media_mediaadtype
# LEFT JOIN
#     app_vertical_media_media
# ON
#     app_vertical_media_mediaadtype.MediaId = app_vertical_media_media.MediaId
# LEFT JOIN
#     app_admin_adunitsize
# ON
#     app_vertical_media_mediaadtype.Size = app_admin_adunitsize.AdunitSizeId
# LEFT JOIN
#     app_admin_adformat
# ON
#     app_vertical_media_mediaadtype.AdFormat = app_admin_adformat.AdFormatId
# LEFT JOIN
#     app_admin_adunitposition
# ON
#     app_vertical_media_mediaadtype.Position = app_admin_adunitposition.AdunitPositionId
# LEFT JOIN
#     app_admin_locationtype
# ON
#     app_vertical_media_mediaadtype.LocationType = app_admin_locationtype.LocationTypeId
# LEFT JOIN
#     app_admin_verticaltype
# ON
#     app_vertical_media_mediaadtype.LocationType = app_admin_verticaltype.VerticalTypeId
# LEFT JOIN
#     app_default_adunitcategory
# ON
#     app_vertical_media_mediaadtype.AdUnitCategory = app_default_adunitcategory.AdUnitCategoryId
# LEFT JOIN
#     app_admin_estimatedreach
# ON
#     app_vertical_media_mediaadtype.AdTypeEstimateReached = app_admin_estimatedreach.EstimatedReachId
# LEFT JOIN
#     app_admin_adunitspecificcategory
# ON
#     app_vertical_media_mediaadtype.SpecificCategory = app_admin_adunitspecificcategory.AdUnitSpecificCategoryId
