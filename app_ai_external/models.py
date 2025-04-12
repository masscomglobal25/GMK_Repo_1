from datetime import datetime
import uuid
from django.db import models

# Create your models here.


class AIFilteredData(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    AIFilteredDataId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    UserId = models.CharField(max_length=50, blank=True, null=True)
    # SQLQuery = models.TextField(blank=True, null=True)
    # Country =  models.CharField(max_length=50, blank=True, null=True)
    # MediaType =  models.CharField(max_length=50, blank=True, null=True)
    # CampaignType =  models.CharField(max_length=300, blank=True, null=True)
    CityRegion =  models.TextField(blank=True, null=True)
    Language =  models.TextField(blank=True, null=True)
    Summary =  models.TextField(blank=True, null=True)
    AIJsonData = models.JSONField(blank=True, null=True)