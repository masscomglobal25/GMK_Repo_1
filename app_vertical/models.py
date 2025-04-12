from datetime import datetime
import uuid
from django.db import models

# Create your models here.


class OutOfHome(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    OutOfHomeId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    PublisherId = models.CharField(blank=True, null=True, max_length=50)
    SiteOwnerName = models.CharField(blank=True, null=True, max_length=300)
    CountryEvent = models.CharField(blank=True, null=True, max_length=300)
    CityRegion = models.CharField(blank=True, null=True, max_length=300)
    Location = models.CharField(blank=True, null=True, max_length=300)
    Size = models.CharField(blank=True, null=True, max_length=300)
    Language = models.TextField(blank=True, null=True)
    EstimateReached = models.CharField(blank=True, null=True, max_length=300)
    BenefitsOfAdvertising = models.TextField(blank=True, null=True)
    PromoVideoLink = models.CharField(blank=True, null=True, max_length=300)
    Availability = models.TextField(blank=True, null=True)

    MediaKit = models.FileField(
        blank=True, null=True, upload_to='vertical/OutOfHome/mediakit')
    MapLink = models.TextField(blank=True, null=True)
    Latitude = models.CharField(blank=True, null=True, max_length=300)
    Longitude = models.CharField(blank=True, null=True, max_length=300)
    IsHyperlocal = models.CharField(blank=True, null=True, max_length=300)
    
    OutOfHomeImage = models.FileField(
        blank=True, null=True, upload_to='vertical/OutOfHome/image')
    Status = models.IntegerField(blank=True, null=True)
    ViewsCount = models.IntegerField(blank=True, null=True)
    ModifiedDate = models.DateTimeField(blank=True, null=True)


class OutOfHomeImage(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    OutOfHomeImageId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    OutOfHomeId = models.CharField(blank=True, null=True, max_length=300)
    OutOfHomeImage = models.FileField(
        blank=True, null=True, upload_to='vertical/OutOfHome/image')


class OutOfHomeMediaAdType(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    OutOfHomeMediaAdTypeId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    OutOfHomeId = models.CharField(blank=True, null=True, max_length=50)
    MediaAdType = models.CharField(blank=True, null=True, max_length=300)
    SiteName = models.CharField(blank=True, null=True, max_length=300)
    LocationType = models.CharField(blank=True, null=True, max_length=300)
    VerticalTypeId = models.CharField(blank=True, null=True, max_length=300)
    NoOfScreen = models.CharField(blank=True, null=True, max_length=300)
    MediaAdUnitDescription = models.TextField(blank=True, null=True)
    IsDigital = models.CharField(blank=True, null=True, max_length=300)
    SingleRotationTime = models.CharField(blank=True, null=True, max_length=10)
    DurationOfCreative = models.CharField(blank=True, null=True, max_length=10)
    LightingType = models.CharField(blank=True, null=True, max_length=300)
    PackageName = models.CharField(blank=True, null=True, max_length=300)
    PackageType = models.CharField(blank=True, null=True, max_length=300)
    StartDate = models.CharField(blank=True, null=True, max_length=300)
    EndDate = models.CharField(blank=True, null=True, max_length=300)
    NoOfDays = models.CharField(blank=True, null=True, max_length=300)
    MonthlyRentalRate = models.CharField(blank=True, null=True, max_length=300)
    Discount = models.CharField(blank=True, null=True, max_length=300)
    NetCostBeforeTax = models.CharField(blank=True, null=True, max_length=300)
    ProductionCost = models.CharField(blank=True, null=True, max_length=300)
    Tax = models.CharField(blank=True, null=True, max_length=300)
    Availability = models.TextField(blank=True, null=True)
    NetCost = models.CharField(blank=True, null=True, max_length=300)
    RateValidaty = models.CharField(blank=True, null=True, max_length=300)
    AdUnitCategory = models.CharField(blank=True, null=True, max_length=50)
    AdTypeMediaKit = models.FileField(
        blank=True, null=True, upload_to='vertical/OutOfHome/mediakit')
    AdTypeEstimateReached = models.CharField(blank=True, null=True, max_length=300)
    NearByAdvantages = models.TextField(blank=True, null=True)
    MatchingCategories = models.TextField(blank=True, null=True)
    AgeGroup = models.TextField(blank=True, null=True)
    GenderGroup = models.TextField(blank=True, null=True)
    PromoVideoLink = models.CharField(blank=True, null=True, max_length=300)
    IncomeGroup = models.TextField(blank=True, null=True)
    NationalityCommunity = models.TextField(blank=True, null=True)
    RunAsOffer = models.CharField(blank=True, null=True, max_length=300)
    IsLocalTaxApplied = models.CharField(blank=True, null=True, max_length=300)
    IsNeedApproval = models.CharField(blank=True, null=True, max_length=300)
    NoOfDaysRequired = models.CharField(blank=True, null=True, max_length=300)
    TermsAndConditions = models.TextField(blank=True, null=True)

    
class OutOfHomeMediaAdTypeImage(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    OutOfHomeMediaAdTypeImageId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    OutOfHomeMediaAdTypeId = models.CharField(blank=True, null=True, max_length=300)
    OutOfHomeMediaAdTypeImage = models.FileField(
        blank=True, null=True, upload_to='vertical/OutOfHome/image')
