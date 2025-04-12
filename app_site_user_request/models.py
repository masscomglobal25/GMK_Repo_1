from datetime import datetime
import uuid
from django.db import models

# Create your models here.


class SiteRequest(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    SiteRequestId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    UserTypeId = models.CharField(max_length=50)
    UserId = models.CharField(max_length=50)
    RequestType = models.CharField(max_length=300)
    Heading = models.TextField()
    Message = models.TextField()
    CreatedDate = models.CharField(max_length=200)