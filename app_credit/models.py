from datetime import datetime
import uuid
from django.db import models
# Create your models here.


class Credits(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    CreditId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    CreditCount = models.CharField(blank=True, null=True, max_length=50)
    Amount = models.CharField(blank=True, null=True, max_length=50)


class AdvertiserCreditRequest(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    CreditRequiredId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    AdvertiserId = models.CharField(blank=True, null=True, max_length=50)
    CreditsRequired = models.CharField(blank=True, null=True, max_length=50)
    TotalPayable = models.CharField(blank=True, null=True, max_length=50)
    Status = models.CharField(blank=True, null=True, max_length=5)
