from datetime import datetime
from tokenize import Name
import uuid
from django.db import models

# Create your models here.


class StaffRegister(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    StaffRegisterId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(blank=True, null=True, max_length=300)
    StaffCode = models.CharField(blank=True, null=True, max_length=300)
    EmailId = models.CharField(blank=True, null=True, max_length=300)
    Address=models.TextField(blank=True, null=True)
    PinCode = models.CharField(blank=True, null=True, max_length=30)
    Phone = models.CharField(blank=True, null=True, max_length=30)
    Permission= models.TextField(blank=True, null=True)

