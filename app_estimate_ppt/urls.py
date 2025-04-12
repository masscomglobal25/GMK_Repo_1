

from django.urls import path, re_path as url
from app_estimate_ppt import views


urlpatterns = [
    path('downloadPPT/', views.estimatePPTDownload),
]
