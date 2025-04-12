from django.urls import path, re_path as url
from app_user_plan import views

urlpatterns = [
    path('CURDSiteUserPlanApi/', views.CURDSiteUserPlanApi),
    url(r'^CURDSiteUserPlanApi/(?P<UserType>[0-9a-zA-Z\-]+)$',
        views.CURDSiteUserPlanApi),
    url(r'^CURDSiteUserPlanApi/(?P<UserType>[0-9a-zA-Z\-]+)/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDSiteUserPlanApi),
    path('CURDSiteUserPlanItemApi/', views.CURDSiteUserPlanItemApi),
    url(r'^CURDSiteUserPlanItemApi/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDSiteUserPlanItemApi),
]
