from datetime import datetime
import uuid
from django.db import models

# Create your models here.


class Vertical(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    VerticalId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    Identification = models.IntegerField(default=1000)
    VerticalName = models.CharField(max_length=300)
    VerticalIcon = models.FileField(
        blank=True, null=True, upload_to='vertical/vertical_icon')
    VerticalIconBW = models.FileField(
        blank=True, null=True, upload_to='vertical/vertical_icon')
    VerticalEmoji = models.FileField(
        blank=True, null=True, upload_to='vertical/vertical_emoji')
    VerticalImage = models.FileField(
        blank=True, null=True, upload_to='vertical/vertical_image')
    VerticalCoverImage = models.FileField(
        blank=True, null=True, upload_to='vertical/cover_image')
    VerticalCoverVideoLink = models.CharField(blank=True, null=True, max_length=300)
    VerticalOrder = models.IntegerField(default=0)
    RefId = models.CharField(max_length=50, blank=True)

class VerticalStatus(models.Model):
    VerticalStatusId = models.AutoField(primary_key=True, editable=False)
    VerticalStatus = models.CharField(max_length=300)


class MediaAdType(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    MediaAdTypeId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    MediaAdType = models.CharField(max_length=300)


class PackageType(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    PackageTypeId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    PackageType = models.CharField(max_length=300)


class LightingType(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    LightingTypeId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    LightingType = models.CharField(max_length=310)


class UserType(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    UserTypeId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    UserType = models.CharField(max_length=300)


class SiteImageResolution(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    ImageResolutionId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    ImageName = models.CharField(max_length=300)
    Width = models.IntegerField()
    Height = models.IntegerField()


class CountryType(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    CountryTypeId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    CountryType = models.CharField(max_length=300)


class AdUnitCategory(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    AdUnitCategoryId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    OrderNo = models.IntegerField(default=0)
    AdUnitCategory = models.CharField(max_length=300)


class TimeZone(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    TimeZoneId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    TimeZone = models.CharField(max_length=300)


class ServiceOrderUnit(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    ServiceOrderUnitId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    ServiceOrderUnit = models.CharField(max_length=300)


class ServiceUnitType(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    ServiceUnitTypeId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    ServiceUnitType = models.CharField(max_length=300)


class StaffPermission(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    StaffPermissionId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    StaffPermission = models.CharField(max_length=300)


class AdvertiserAssistanceSupport(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    AssistanceId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    AssistanceIcon = models.FileField(
        blank=True, null=True, upload_to='assistanceSupport/vertical_image')
    AssistanceName = models.TextField()
    InfoLabel = models.TextField(blank=True, null=True)
    SupportBy = models.CharField(max_length=300)
    CreditsRequired = models.CharField(max_length=10)


class OrganisationType(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    OrganisationTypeId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    OrganisationType = models.CharField(max_length=300)


class BotAavatar(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    BotAavatarId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    BotAavatar = models.FileField(
        blank=True, null=True, upload_to='bot/default')
