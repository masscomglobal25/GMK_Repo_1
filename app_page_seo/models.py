from django.db import models
from datetime import datetime
import uuid
# Create your models here.


class PageSeo(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    PageSeoId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    PageName = models.CharField(max_length=300, blank=True, null=True)
    SEOMetaTitle = models.TextField(blank=True, null=True)
    SEOMetaDescription = models.TextField(blank=True, null=True)
    SEOMetaKeyword = models.TextField(blank=True, null=True)


class BoutiquePageSeo(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    BoutiquePageSeoId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    CountryId = models.CharField(max_length=50, blank=True, null=True)
    AudienceId = models.CharField(max_length=50, blank=True, null=True)
    SEOMetaTitle = models.TextField(blank=True, null=True)
    SEOMetaDescription = models.TextField(blank=True, null=True)
    SEOMetaKeyword = models.TextField(blank=True, null=True)
