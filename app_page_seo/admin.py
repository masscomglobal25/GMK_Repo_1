from django.contrib import admin

from app_page_seo.models import PageSeo

# Register your models here.

class PageSeoAdmin(admin.ModelAdmin):
    list_display = ('PageName', 'PageSeoId')


admin.site.register(PageSeo, PageSeoAdmin)
