from django.contrib import admin

from app_site.models import SiteSettings

# Register your models here.


class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('DefaultCountry','DefaultCurrency','DefaultTimeZone','DraftExpiryDays','PaymentPendingExpiryDays','DefaultAdvertiserCredits')


admin.site.register(SiteSettings, SiteSettingsAdmin)

