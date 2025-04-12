from datetime import datetime
import uuid
from django.db import models

# Create your models here.

class UserSitePlan(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    SitePlanId = models.AutoField(primary_key=True, editable=False)
    PlanName = models.CharField(max_length=300, blank=True, null=True)
    PlanDetails = models.TextField( blank=True, null=True)
    UserTypeId = models.CharField(max_length=50, blank=True, null=True)
    Validity = models.IntegerField(blank=True, null=True)
    Currency = models.CharField(max_length=50, blank=True, null=True)
    Amount = models.IntegerField(blank=True, null=True)
    Credit = models.IntegerField(blank=True, null=True)
    Status = models.IntegerField(default=0,blank=True, null=True)
    OpportunityCountInPlan = models.IntegerField(default=0,blank=True, null=True)

class UserSitePlanItem(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    SitePlanItemId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    ItemName = models.CharField(max_length=300, blank=True, null=True)
    Status = models.IntegerField(default=0,blank=True, null=True)
