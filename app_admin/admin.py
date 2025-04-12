from django.contrib import admin

from .models import CampaignUnit, CountryEvent, StaffRegister, CityRegion, VerticalType, Language, EstimatedReach, LocationType, NearByAdvantage

# Register your models here.

admin.site.register(CountryEvent)
admin.site.register(StaffRegister)
admin.site.register(CityRegion)
admin.site.register(VerticalType)
admin.site.register(Language)
admin.site.register(EstimatedReach)
admin.site.register(LocationType)
admin.site.register(NearByAdvantage)
admin.site.register(CampaignUnit)
