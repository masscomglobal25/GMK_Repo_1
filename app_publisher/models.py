from datetime import datetime
import uuid
from django.db import models

# Create your models here.


class PublisherRegister(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    PublisherId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    MediaName = models.CharField(max_length=300, blank=True, null=True)
    CompanyName = models.CharField(max_length=300, blank=True, null=True)
    TimeZone = models.CharField(max_length=50, blank=True, null=True)
    BusinessEmail = models.CharField(max_length=200, blank=True, null=True)
    OfficeLocation = models.CharField(max_length=300, blank=True, null=True)
    Country = models.CharField(max_length=300, blank=True, null=True)
    Website = models.CharField(max_length=300, blank=True, null=True)
    ContactName = models.CharField(max_length=300, blank=True, null=True)
    Position = models.CharField(max_length=300, blank=True, null=True)
    BusinessName = models.CharField(max_length=300, blank=True, null=True)
    MobileCode = models.CharField(max_length=10, blank=True, null=True)
    DefaultCurrency = models.CharField(max_length=30, blank=True, null=True)
    MobileNumber = models.CharField(max_length=30, blank=True, null=True)
    Status = models.CharField(max_length=300, blank=True, null=True)
    ContactsOnOff =  models.IntegerField(blank=True, null=True)
    BannerImage = models.FileField(
        blank=True, null=True, upload_to='publisher/banner_image') 
    BannerImageForMobile = models.FileField(
        blank=True, null=True, upload_to='publisher/banner_image') 
    Description  = models.TextField(blank=True, null=True)
    Title  = models.TextField(blank=True, null=True)
    SeoDescription  = models.TextField(blank=True, null=True)
    Keywords = models.TextField(blank=True, null=True)
    ProfileImage = models.FileField(
        blank=True, null=True, upload_to='publisher/profile')
    RegBy = models.CharField(max_length=30, blank=True, null=True)
    UserName = models.CharField(max_length=100, blank=True, null=True)
    PlanStatus =  models.IntegerField(blank=True, null=True,default=0)
    #0=Free,1=Enterprise,2=Franchase,3=SAAS
    PlanExpiryDate =  models.CharField(max_length=200,blank=True, null=True)
    EnableBot =  models.BooleanField(blank=True, null=True,default=False)
    BotName =  models.CharField(max_length=200,blank=True, null=True)
    BotAavatar =  models.CharField(max_length=300,blank=True, null=True)
    EnableMailUpdates =  models.BooleanField(default=False)
    EnableMediaEntry =  models.BooleanField(default=False)


class PublisherContact(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    PublisherContactId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    PublisherId = models.CharField(max_length=50)
    Name = models.CharField(max_length=300, blank=True, null=True)
    Designation = models.CharField(max_length=300, blank=True, null=True)
    BioData = models.TextField(blank=True, null=True)
    Expertise = models.TextField(blank=True, null=True)
    Language = models.TextField(blank=True, null=True)
    Email = models.CharField(max_length=300, blank=True, null=True)
    PhoneCode = models.CharField(max_length=10, blank=True, null=True)
    PhoneNumber = models.CharField(max_length=300, blank=True, null=True)
    CountriesHandled = models.TextField(blank=True, null=True)
    LocationHandled = models.TextField(blank=True, null=True)
    TimeZone = models.CharField(max_length=50, blank=True, null=True)
    ProfileImage = models.FileField(
        blank=True, null=True, upload_to='publisher/profile')


class MeetingRequest(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    MeetingRequestId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    AdvertiserId = models.CharField(max_length=50)
    PublisherId = models.CharField(max_length=50)
    MediaId = models.CharField(max_length=50, blank=True, null=True)
    PublisherContactId = models.CharField(max_length=50)
    PreferredContact = models.CharField(max_length=50)
    HelpRequiredFor = models.TextField()
    FromDate = models.CharField(max_length=50)
    FromTime = models.CharField(max_length=50)
    ToDate = models.CharField(max_length=50)
    ToTime = models.CharField(max_length=50)
    TimeZone = models.CharField(max_length=100)
    Message = models.TextField()
    CreatedDate = models.CharField(max_length=200)
    Status = models.IntegerField(blank=True, null=True)