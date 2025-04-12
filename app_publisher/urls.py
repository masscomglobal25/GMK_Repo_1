from django.urls import path, re_path as url
from app_publisher import views


urlpatterns = [
    
    url(r'^PublisherDetailByUsername/(?P<UserName>[0-9a-zA-Z\-]+)$',
        views.PublisherDetailByUsername),

    path('CURDPublisherRegister/', views.CURDPublisherRegisterApi),
    path('CURDPublisherProfile/', views.CURDPublisherProfileApi),
    url(r'^CURDPublisherProfile/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDPublisherProfileApi),
    url(r'^UploadPublisherProfile/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.UploadPublisherProfileFileView.as_view()),

    url(r'^UploadPublisherSeoBanner/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.UploadPublisherSeoBannerFileView.as_view()),

    url(r'^UploadPublisherSeoBannerForMoblie/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.UploadPublisherSeoBannerForMoblieFileView.as_view()),

    path('CURDPublisherURL/', views.CURDPublisherProfileURlApi),
    path('CURDPublisherSEO/', views.CURDPublisherProfileSEOApi),
        
    path('CURDPublisherMCCount/', views.CURDPublisherMCCountApi),

    
    path('CURDPublisherContact/', views.CURDPublisherContactApi),
    url(r'^CURDPublisherContact/(?P<PublisherId>[0-9a-zA-Z\-]+)$',
        views.CURDPublisherContactApi),
    url(r'^CURDPublisherContact/(?P<PublisherId>[0-9a-zA-Z\-]+)/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDPublisherContactApi),
    # url(r'^CURDPublisherContact2/(?P<PublisherId>[0-9a-zA-Z\-]+)$/(?P<pk>[0-9a-zA-Z\-]+)$',
    #     views.CURDPublisherContactApi),
    url(r'^CURDPublisherContactImage/$', views.PublisherContactFileView.as_view(), name='file-upload'),
    url(r'^CURDPublisherContactImage/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.PublisherContactFileView.as_view()),
        

    path('CURDMeetingRequest/', views.CURDMeetingRequestApi),
    url(r'^CURDMeetingRequestByPublisher/(?P<PublisherId>[0-9a-zA-Z\-]+)$',
        views.CURDMeetingRequestApi),
    url(r'^CURDMeetingRequestByAdvertiser/(?P<AdvertiserId>[0-9a-zA-Z\-]+)$',
        views.CURDMeetingRequestByAdvertiserApi),
    url(r'^CURDMeetingRequest/(?P<PublisherId>[0-9a-zA-Z\-]+)/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDMeetingRequestApi),
    url(r'^CURDMeetingRequestAdvertiserMedia/(?P<MediaId>[0-9a-zA-Z\-]+)/(?P<AdvertiserId>[0-9a-zA-Z\-]+)$',
        views.CURDMeetingRequestAdvertiserMedia),
]
# CURDPublisherContactImage