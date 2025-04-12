from datetime import datetime
from enum import unique
import uuid
from django.db import models

# Create your models here.


class AdBuzz(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    AdBuzzId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    UserId = models.CharField(max_length=50, blank=True, null=True)
    UserType = models.CharField(max_length=50, blank=True, null=True)
    Heading = models.TextField(blank=True, null=True)
    Content = models.TextField(blank=True, null=True)
    CountrySelect = models.CharField(max_length=50, blank=True, null=True)
    AdbuzzTagging = models.CharField(max_length=50, blank=True, null=True)
    AdbuzzCategory = models.CharField(max_length=50, blank=True, null=True)
    UploadOption = models.CharField(max_length=50, blank=True, null=True)
    VideoLink = models.CharField(max_length=400, blank=True, null=True)
    LikeCount = models.IntegerField(default=0)
    ShareCount = models.IntegerField(default=0)
    ViewCount = models.IntegerField(default=0)
    CreatedDate = models.DateTimeField(default=datetime.now)
    UpdatedDate = models.DateTimeField(default=datetime.now)
    EnableComment = models.BooleanField(default=False)
    Status = models.IntegerField(default=0)# 0=pending,1=approved,-1=rejected
    SeoTitle = models.TextField(blank=True, null=True)
    SeoDescription = models.TextField(blank=True, null=True)
    SeoKeywords = models.TextField(blank=True, null=True)
    LikedUser = models.TextField(blank=True, null=True)

class AdBuzzImage(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    AdBuzzImageId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    AdBuzzId = models.CharField(max_length=50, blank=True, null=True)
    AdBuzzImageName = models.FileField(
        blank=True, null=True, upload_to='ad-buzz')