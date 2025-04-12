from django.urls import path, re_path as url
from app_advertiser import views


urlpatterns = [
    path('CURDAdvertiserRegister/', views.CURDAdvertiserRegisterApi),
    path('CURDAdvertiserProfile/', views.CURDAdvertiserProfileApi),
    url(r'^GetCreditCount/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.GetCreditCount),
    path('UpdateCreditCount/', views.UpdateCreditCount),
    url(r'^CURDAdvertiserProfile/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDAdvertiserProfileApi),
    url(r'^UploadAdvertiserProfile/(?P<pk>[0-9a-zA-Z\-]+)$', views.UploadAdvertiserProfileFileView.as_view(), name='file-upload'),
]