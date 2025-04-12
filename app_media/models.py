from datetime import datetime
from locale import currency
import uuid
from django.db import models

# Create your models here.


class Cart(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    CartId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    AdvertiserId = models.CharField(max_length=50, null=True)
    MediaAdTypeId = models.CharField(max_length=50, null=True)
    StartDate = models.CharField(max_length=200, null=True)
    MediaLink = models.TextField(blank=True, null=True)
    MediaAdUnitLink = models.TextField(blank=True, null=True)
    CartType = models.IntegerField()
    CartStatus = models.IntegerField()
    MediaDetail = models.TextField()
    MediaAdTypeDetail = models.TextField()
    Vertical = models.CharField(max_length=50, null=True)
    Amount = models.CharField(max_length=20)


class Plan(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    PlanId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    AdvertiserId = models.CharField(max_length=50, null=True)
    AdvertiserDetails = models.TextField(blank=True, null=True)
    PlanName = models.CharField(max_length=400, null=True)
    BrandName = models.CharField(max_length=400, null=True, blank=True)
    BrandCategory = models.TextField(null=True, blank=True)
    CreatedByUserType = models.CharField(max_length=50, null=True)
    CreatedByUserId = models.CharField(max_length=50, null=True)
    CampaignObjective = models.TextField(null=True, blank=True)
    SourceFrom = models.IntegerField()  # 0=GMK/1=media store
    StartDate = models.CharField(max_length=50, null=True)
    EstimateAmount = models.CharField(max_length=20, null=True)
    Currency = models.CharField(max_length=10, null=True)
    Status = models.IntegerField(default=0)
    Approval = models.IntegerField(default=0)
    Payment = models.IntegerField(default=0)
    Creative = models.IntegerField(default=0)
    PlanCreatedDate = models.CharField(max_length=50, null=True)
    PlanExpiryDate = models.CharField(max_length=50, null=True)
    CreativeDocFile = models.CharField(max_length=400, null=True)
    PaidExcelDownload = models.IntegerField(default=0)
    AdvertiserAssistanceSupport = models.TextField(null=True)
    AssistanceSupportCreditUsed = models.CharField(max_length=20, null=True)


class PlanDetail(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    PlanDetailId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    PlanId = models.CharField(max_length=50, blank=True, null=True)
    AdvertiserId = models.CharField(max_length=50, blank=True, null=True)
    MediaAdTypeId = models.CharField(max_length=50, blank=True, null=True)
    StartDate = models.CharField(max_length=200, blank=True, null=True)
    MediaLink = models.TextField(blank=True, null=True)
    MediaAdUnitLink = models.TextField(blank=True, null=True)
    SourceFrom = models.IntegerField()  # 0=GMK/1=media store
    ExpiryDate = models.CharField(max_length=200, blank=True, null=True)
    MediaDetail = models.TextField(blank=True, null=True)
    MediaAdTypeDetail = models.TextField(blank=True, null=True)
    Vertical = models.CharField(max_length=50, blank=True, null=True)
    Amount = models.CharField(max_length=20, blank=True, null=True)
    CampaignUnit = models.TextField(blank=True, null=True)
    TotalServedCount = models.IntegerField(default=0)
    Status = models.IntegerField(default=0)
    # 0= Draft,1=send for approval, 2 approval,3= accpected by advertizer,4= booked, 5 =start campaign,6 = end campaign,7=cancell in between campaign


class EstimateShorten(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    EstimateShortenId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    PlanId = models.CharField(max_length=50, null=True)
    AdvertiserId = models.CharField(max_length=50, null=True)
    PlanName = models.CharField(max_length=50, null=True)


class CampaignReportRegister(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    CampaignReportRegisterId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    PlanId = models.CharField(max_length=50, null=True)
    PlanDetailId = models.CharField(max_length=50, null=True)
    ReportType = models.CharField(max_length=50, null=True)
    StartDate = models.CharField(max_length=50, blank=True, null=True)
    EndDate = models.CharField(max_length=50, blank=True, null=True)
    UploadProof = models.FileField(
        blank=True, null=True, upload_to='campaign/report_proof')
    ProofLink = models.TextField(blank=True, null=True)


class CampaignReportDetail(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    CampaignReportDetailId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    CampaignReportRegisterId = models.CharField(max_length=50, null=True)
    Unit = models.CharField(max_length=50, blank=True,null=True)
    OtherUnit = models.CharField(max_length=300,blank=True, null=True)
    ServedCount = models.CharField(max_length=50, blank=True,null=True)
