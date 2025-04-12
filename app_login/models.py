from datetime import datetime
from enum import unique
import uuid
from django.db import models
from django.forms import IntegerField

# Create your models here.


class Login(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    LoginId = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    UserId = models.CharField(max_length=50)
    UserType = models.CharField(max_length=50)
    EmailId = models.CharField(max_length=200)
    Password = models.CharField(max_length=300)
    Token = models.CharField(max_length=300)
    Status = models.IntegerField()


class UserTokenRegister(models.Model):
    SortId = models.DateTimeField(editable=False, default=datetime.now)
    TokenId = models.CharField(
        max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    LoginId = models.CharField(max_length=50, null=True, blank=True)
    UserType = models.CharField(max_length=50, null=True, blank=True)
    EmailId = models.CharField(max_length=150, null=True, blank=True)
    LoginType = models.CharField(max_length=50, null=True, blank=True)
