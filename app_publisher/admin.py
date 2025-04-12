from django.contrib import admin

from .models import PublisherContact, PublisherRegister

# Register your models here.

admin.site.register(PublisherContact)
admin.site.register(PublisherRegister)