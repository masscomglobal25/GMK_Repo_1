from datetime import datetime
import uuid
from django.db import models

# Create your models here.


class SalesMarketing(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    SalesMarketingId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    ConnectedTo = models.CharField(
        max_length=50, blank=True, null=True)  # Publisher/Advertiser
    CompanyName = models.CharField(max_length=300, blank=True, null=True)
    MediaName = models.CharField(max_length=300, blank=True, null=True)
    Country = models.CharField(max_length=50, blank=True, null=True)
    Email = models.CharField(max_length=300, blank=True, null=True)
    Phone = models.CharField(max_length=300, blank=True, null=True)
    IsAccountCreated = models.IntegerField(blank=True, null=True)
    ConnectedPersonId = models.CharField(max_length=50, blank=True, null=True)
    Status = models.CharField(max_length=50,
                              blank=True, null=True)
    Health = models.CharField(max_length=50, blank=True, null=True)
    # cold, warm, hot, cool
    JoinedDate = models.CharField(max_length=300, blank=True, null=True)


class SalesMarketingDetail(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    SalesMarketingDetailId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    SalesMarketingId = models.CharField(max_length=50, blank=True, null=True)
    UserId = models.CharField(max_length=50, blank=True, null=True)
    UserType = models.CharField(max_length=50,
                                blank=True, null=True)
    # Email,Phone, Online meeting, direct meeting
    ConnectedThrough = models.CharField(max_length=50,
                                        blank=True, null=True)
    # Init connection,Followup,Support etc.
    ConnectedType = models.CharField(max_length=300, blank=True, null=True)
    MeetingFeedback = models.TextField(blank=True, null=True)
    DetailsShared = models.TextField(blank=True, null=True)
    Comments = models.TextField(blank=True, null=True)
    Status = models.CharField(max_length=50,
                              blank=True, null=True)
    Health = models.CharField(max_length=50, blank=True, null=True)
    # cold, warm, hot, cool
    CreatedDate = models.CharField(max_length=300, blank=True, null=True)
