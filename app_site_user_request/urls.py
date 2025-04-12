from django.urls import path, re_path as url
from app_site_user_request import views

urlpatterns = [
    path('CURDSiteRequestApi/', views.CURDSiteRequestApi),
    url(r'^CURDSiteRequestApi/(?P<UserType>[0-9a-zA-Z\-]+)$',
        views.CURDSiteRequestApi),
    url(r'^CURDSiteRequestApi/(?P<UserType>[0-9a-zA-Z\-]+)/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDSiteRequestApi),
]
