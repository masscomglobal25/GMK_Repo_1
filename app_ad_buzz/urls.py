from django.urls import path, re_path as url
from app_ad_buzz import views


urlpatterns = [
    path('CURDAdBuzz/', views.CURDAdBuzzApi),
    url(r'^CURDAdBuzz/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDAdBuzzApi),
    path('UploadAdBuzz/', views.UploadAdBuzzFileView.as_view(), name='file-upload'),
    url(r'^UploadAdBuzz/(?P<pk>[0-9a-zA-Z\-]+)$', views.UploadAdBuzzFileView.as_view(), name='file-upload'),
    
    url(r'^CURDAdBuzzImage/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDAdBuzzImageApi),
    url(r'^CURDAdBuzzTrending/',
        views.CURDAdBuzzTrendingApi),
    url(r'^GetAdBuzzByTagging/(?P<AdbuzzTagging>[0-9a-zA-Z\-]+)$',
        views.GetAdBuzzByTagging),
]