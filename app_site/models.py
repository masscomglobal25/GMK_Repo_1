from datetime import datetime
import uuid
from django.db import models

# Create your models here.


class Log(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    LogId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    Content = models.TextField(blank=True, null=True)
    UserType = models.CharField(blank=True, null=True, max_length=50)
    UserName = models.CharField(blank=True, null=True, max_length=300)
    UserId = models.CharField(blank=True, null=True, max_length=50)
    LogType = models.CharField(blank=True, null=True, max_length=300)
    JsonData = models.TextField(blank=True, null=True)
    CretedDate = models.CharField(blank=True, null=True, max_length=50)


class SiteSettings(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    SiteSettingId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    DefaultCountry = models.CharField(blank=True, null=True, max_length=50)
    DefaultListingCountry = models.CharField(
        blank=True, null=True, max_length=50)
    DefaultListingVertical = models.CharField(
        blank=True, null=True, max_length=50)
    DefaultCurrency = models.CharField(blank=True, null=True, max_length=50)
    DefaultTimeZone = models.CharField(blank=True, null=True, max_length=50)
    DraftExpiryDays = models.CharField(blank=True, null=True, max_length=50)
    PaymentPendingExpiryDays = models.CharField(
        blank=True, null=True, max_length=50)
    DefaultAdvertiserCredits = models.CharField(
        blank=True, null=True, max_length=50)
    CreditsExpiryDays = models.CharField(blank=True, null=True, max_length=50)
    ExcelCredits = models.CharField(blank=True, null=True, max_length=50)
    FreeCreditOnRequest = models.IntegerField(default=0)
    Priority100Enable = models.IntegerField(default=0)
    PlanItemDatePickerEnable = models.IntegerField(default=0)
    UploadingImageSize = models.CharField(blank=True, null=True, max_length=50)
    UploadingAudioSize = models.CharField(blank=True, null=True, max_length=50)
    UploadingMediaKitSize = models.CharField(
        blank=True, null=True, max_length=50)
    AdOpportunityPrompt = models.TextField(blank=True, null=True)
    MediaLocationPrompt = models.TextField(blank=True, null=True)
    InitRedirectionLink = models.TextField(blank=True, null=True)
    NoOfOpportunitiesPerPlanEnterprise = models.IntegerField(default=20)
    NoOfOpportunitiesPerPlanNormal = models.IntegerField(default=10)
    VerticalSpecificCategoryOrder = models.TextField(blank=True, null=True)


class CampaignPDFData(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    PDFDataId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    UserId = models.CharField(blank=True, null=True, max_length=50)
    CampaignId = models.CharField(blank=True, null=True, max_length=50)
    PDFData = models.TextField(blank=True, null=True)


class Comments(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    CommentId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    FromId = models.CharField(blank=True, null=True, max_length=50)
    FromUserTypeId = models.CharField(blank=True, null=True, max_length=50)
    CommentType = models.CharField(blank=True, null=True, max_length=50)
    TypeId = models.CharField(blank=True, null=True, max_length=50)
    CommentDate = models.CharField(blank=True, null=True, max_length=300)
    Comments = models.TextField(blank=True, null=True)


class PriorityCode(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    PriorityCodeId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    PriorityCode = models.CharField(blank=True, null=True, max_length=300)
