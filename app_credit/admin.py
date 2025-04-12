from django.contrib import admin

from app_credit.models import Credits

# Register your models here.

class CreditsAdmin(admin.ModelAdmin):
    list_display = ('CreditCount', 'Amount')


admin.site.register(Credits, CreditsAdmin)
