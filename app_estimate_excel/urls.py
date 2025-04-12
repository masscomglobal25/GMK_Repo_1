

from django.urls import path, re_path as url
from app_estimate_excel import views


urlpatterns = [
    path('downloadExcel/', views.downloadExcel),
]
