from django.urls import path, re_path as url
from app_gmk_staff import views

urlpatterns = [
    path('CURDStaffRegister/', views.CURDStaffRegisterApi),
    url(r'^CURDStaffRegister/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDStaffRegisterApi),
]
