from django.contrib import admin

from .models import AdUnitCategory, AdvertiserAssistanceSupport, BotAavatar, CountryType, MediaAdType, OrganisationType, ServiceOrderUnit, ServiceUnitType, SiteImageResolution, StaffPermission, TimeZone, Vertical, PackageType, LightingType, UserType, VerticalStatus

# Register your models here.


class VerticalAdmin(admin.ModelAdmin):
    list_display = ('VerticalName', 'VerticalId', 'RefId')


admin.site.register(Vertical, VerticalAdmin)


class MediaAdTypeAdmin(admin.ModelAdmin):
    list_display = ('MediaAdType', 'MediaAdTypeId')


admin.site.register(MediaAdType, MediaAdTypeAdmin)


class PackageTypeAdmin(admin.ModelAdmin):
    list_display = ('PackageType', 'PackageTypeId')


admin.site.register(PackageType, PackageTypeAdmin)


class LightingTypeAdmin(admin.ModelAdmin):
    list_display = ('LightingType', 'LightingTypeId')


admin.site.register(LightingType, LightingTypeAdmin)


class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('UserType', 'UserTypeId')


admin.site.register(UserType, UserTypeAdmin)


class SiteImageResolutionAdmin(admin.ModelAdmin):
    list_display = ('ImageName', 'Width', 'Height')


admin.site.register(SiteImageResolution, SiteImageResolutionAdmin)


class CountryTypeAdmin(admin.ModelAdmin):
    list_display = ('CountryType', 'CountryTypeId')


admin.site.register(CountryType, CountryTypeAdmin)


class VerticalStatusAdmin(admin.ModelAdmin):
    list_display = ('VerticalStatusId', 'VerticalStatus')


admin.site.register(VerticalStatus, VerticalStatusAdmin)


class AdUnitCategoryAdmin(admin.ModelAdmin):
    list_display = ('AdUnitCategory', 'AdUnitCategoryId')


admin.site.register(AdUnitCategory, AdUnitCategoryAdmin)


class TimeZoneAdmin(admin.ModelAdmin):
    list_display = ('TimeZone', 'TimeZoneId')


admin.site.register(TimeZone, TimeZoneAdmin)


class ServiceUnitTypeAdmin(admin.ModelAdmin):
    list_display = ('ServiceUnitType', 'ServiceUnitTypeId')


admin.site.register(ServiceUnitType, ServiceUnitTypeAdmin)


class ServiceOrderUnitAdmin(admin.ModelAdmin):
    list_display = ('ServiceOrderUnit', 'ServiceOrderUnitId')


admin.site.register(ServiceOrderUnit, ServiceOrderUnitAdmin)


class AdvertiserAssistanceSupportAdmin(admin.ModelAdmin):
    list_display = ('AssistanceName', 'SupportBy',
                    'CreditsRequired', 'AssistanceId')


admin.site.register(AdvertiserAssistanceSupport,
                    AdvertiserAssistanceSupportAdmin)


class StaffPermissionAdmin(admin.ModelAdmin):
    list_display = ('StaffPermission', 'StaffPermissionId')


admin.site.register(StaffPermission, StaffPermissionAdmin)


class OrganisationTypeAdmin(admin.ModelAdmin):
    list_display = ('OrganisationType', 'OrganisationTypeId')


admin.site.register(OrganisationType, OrganisationTypeAdmin)

class BotAavatarAdmin(admin.ModelAdmin):
    list_display = ('BotAavatar', 'BotAavatarId')


admin.site.register(BotAavatar, BotAavatarAdmin)
