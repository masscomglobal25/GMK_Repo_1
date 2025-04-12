from datetime import datetime
import uuid
from django.db import models

# Create your models here.


class Profile(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    AdvertiserId = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    FirstName = models.CharField(max_length=300, blank=True, null=True)
    LastName = models.CharField(max_length=300, blank=True, null=True)
    BusinessEmail = models.CharField(max_length=200, blank=True, null=True)
    CompanyName = models.CharField(max_length=300, blank=True, null=True)
    BuildingNo = models.CharField(max_length=300, blank=True, null=True)
    StreetAddress = models.TextField(blank=True, null=True)
    City = models.CharField(max_length=300, blank=True, null=True)
    State = models.CharField(max_length=300, blank=True, null=True)
    ZIPCode = models.CharField(max_length=10, blank=True, null=True)
    Country = models.CharField(max_length=50, blank=True, null=True)
    PhoneNumber = models.CharField(max_length=20, blank=True, null=True)
    PhoneCode = models.CharField(max_length=10, blank=True, null=True)
    TargetCountries = models.TextField(blank=True, null=True)
    OrganisationType = models.TextField(blank=True, null=True)
    TargetAudience = models.TextField(blank=True, null=True)
    Status = models.IntegerField(blank=True, null=True)
    ProfileImage = models.FileField(
        blank=True, null=True, upload_to='advertiser/profile')
    SMPicture = models.TextField(blank=True, null=True)
    TargetAudience = models.TextField(blank=True, null=True)
    Credits = models.IntegerField(blank=True, null=True)
    CreditsExpiryDate = models.DateTimeField(blank=True, null=True)
    IsUpgrade = models.IntegerField(blank=True, null=True,default=1)
    EnableMailUpdates =  models.BooleanField(default=False)
