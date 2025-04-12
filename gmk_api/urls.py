"""gmk_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.contrib import admin
from django.urls import path, re_path as url
from django.views.static import serve
from django.conf import settings

from django.urls import include

admin.site.site_header = 'GMK Developer Administration'                    # default: "Django Administration"
admin.site.index_title = 'Global Media Kit'                 # default: "Site administration"
admin.site.site_title = 'Developer Administration' # default: "Django site admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-login/', include('app_login.urls')),
    path('api-default/', include('app_default.urls')),
    path('api-admin/', include('app_admin.urls')),
    path('api-vertical/', include('app_vertical.urls')),
    path('api-media/', include('app_media.urls')),
    path('api-advertiser/', include('app_advertiser.urls')),
    path('api-publisher/', include('app_publisher.urls')),
    path('api-estimate/', include('app_estimate.urls')),
    path('api-vertical-media/', include('app_vertical_media.urls')),
    path('api-staff-register/', include('app_gmk_staff.urls')),
    path('api-site/', include('app_site.urls')),
    path('api-credit/', include('app_credit.urls')),
    path('api-site-mail/', include('app_send_mail.urls')),
    path('api-cron-job/', include('app_cron_job.urls')),
    path('api-invoice/', include('app_invoice.urls')),
    path('api-estimate-excel/', include('app_estimate_excel.urls')),
    path('api-gpt/', include('app_chat_gpt.urls')),
    path('api-sales_marketing/', include('app_sales_marketing.urls')),
    path('api-adbuzz/', include('app_ad_buzz.urls')),
    path('api-user-plan/', include('app_user_plan.urls')),
    path('api-estimate-ppt/', include('app_estimate_ppt.urls')),
    path('api-page-seo/', include('app_page_seo.urls')),
    path('api-campaign-report/', include('app_campaign_report.urls')),
    # url(r'^',include('app_login.urls'))
    # path('', admin.site.urls), 
     path('api-ai-external/', include('app_ai_external.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})
]

# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
