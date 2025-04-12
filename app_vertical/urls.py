from django.urls import path, re_path as url
from app_vertical import views

urlpatterns = [
    path('CURDOutOfHome/', views.CURDOutOfHomeApi),
    url(r'^CURDOutOfHome/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDOutOfHomeApi),
    url(r'^CURDPublisherOutOfHome/(?P<PublisherId>[0-9a-zA-Z\-]+)$',
        views.CURDPublisherOutOfHome),

    url(r'^CURDOutOfHomeImage/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.OutOfHomeFileView.as_view()),
    url(r'^CURDOutOfHomeImage/(?P<pk>[0-9a-zA-Z\-]+)/(?P<ImageId>[0-9a-zA-Z\-]+)$',
        views.OutOfHomeFileView.as_view()),

    path('CURDOutOfHomeMediaAdType/', views.CURDOutOfHomeMediaAdTypeApi),
    url(r'^CURDOutOfHomeMediaAdType/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDOutOfHomeMediaAdTypeApi),
    url(r'^CURDOutOfHomeMediaAdType/(?P<outOfHomeId>[0-9a-zA-Z\-]+)$/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDOutOfHomeMediaAdTypeApi),
    url(r'^uploadOutOfHomeMediaAdType/$', views.OutOfHomeMediaAdTypeFileView.as_view(), name='file-upload'),
    url(r'^uploadOutOfHomeMediaAdType/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.OutOfHomeMediaAdTypeFileView.as_view()),


    path('CURDOutOfHomeMediaAdTypeImage/', views.CURDOutOfHomeMediaAdTypeImageApi),
    url(r'^uploadOutOfHomeMediaAdTypeImage/$', views.OutOfHomeMediaAdTypeImageFileView.as_view(), name='file-upload'),
    url(r'^uploadOutOfHomeMediaAdTypeImage/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.OutOfHomeMediaAdTypeImageFileView.as_view()),
    # path('CURDOutOfHomeImage/', views.CURDOutOfHomeImageAPi),
]
