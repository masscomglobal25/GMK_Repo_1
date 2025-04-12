from django.urls import path, re_path as url
from app_cron_job import views

urlpatterns = [
    path('rest-credits/', views.RestCredits),
]
