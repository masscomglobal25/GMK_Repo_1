

from django.urls import path, re_path as url
from app_campaign_report import views


urlpatterns = [
    path('downloadExcelReport/', views.downloadExcel),
    path('downloadPPTReport/', views.downloadPPT),
]
