from django.urls import path, re_path as url
from app_vertical_media import views


urlpatterns = [
    path('AllMedia/', views.AllMediaApi),
    path('CURDMedia/', views.CURDMediaApi),
    path('MediaAdTypeWithMediaViewExcel/', views.download_excel_view),
    path('getMediaData/', views.getMediaData),


    url(r'^ManageMediaListing/(?P<Limit>[0-9a-zA-Z\-]+)/(?P<offset>[0-9a-zA-Z\-]+)$',
        views.ManageMediaListingApi2),
    url(r'^ManageMediaListing2/(?P<Limit>[0-9a-zA-Z\-]+)/(?P<offset>[0-9a-zA-Z\-]+)$',
        views.ManageMediaListingApi2),



    url(r'^CURDMediaDetails/(?P<MediaId>[0-9a-zA-Z\-]+)$',
        views.CURDMediaDetailsApi),
    url(r'^CURDMedia/(?P<VerticalId>[0-9a-zA-Z\-]+)$',
        views.CURDMediaApi),
    url(r'^CURDMedia/(?P<VerticalId>[0-9a-zA-Z\-]+)/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDMediaApi),
    url(r'^CURDMediaIdentification/(?P<VerticalId>[0-9a-zA-Z\-]+)/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDMediaIdentification),

    url(r'^AdminMediaListingApi/(?P<VerticalId>[0-9a-zA-Z\-]+)$',
        views.AdminMediaListingApi),
    url(r'^PublisherMediaListingApi/',
        views.PublisherMediaListingApi),

    url(r'^MediaStatusCountById/(?P<MediaId>[0-9a-zA-Z\-]+)$',
        views.MediaStatusCountByIdApi),




    url(r'^MediaListingAudienceApi/(?P<AudienceId>[0-9a-zA-Z\-]+)/(?P<CountryId>[0-9a-zA-Z\-]+)/(?P<Limit>[0-9a-zA-Z\-]+)/(?P<offset>[0-9a-zA-Z\-]+)$',
        views.MediaListingAudienceApi),
    url(r'^MediaListing/(?P<VerticalId>[0-9a-zA-Z\-]+)/(?P<CountryId>[0-9a-zA-Z\-]+)/(?P<Limit>[0-9a-zA-Z\-]+)/(?P<offset>[0-9a-zA-Z\-]+)$',
        views.MediaListingApi),
    path('MediaForSpecificCategory/', views.MediaForSpecificCategoryApi),
    path('aiMedia/', views.aiMediaForViewAllApi),
    path('AIRecommendedAdUnitApi/', views.AIRecommendedAdUnitApi),


    url(r'^CURDPublisherMedia/(?P<PublisherId>[0-9a-zA-Z\-]+)$',
        views.CURDPublisherMedia),
    url(r'^CURDPublisherMedia/(?P<PublisherId>[0-9a-zA-Z\-]+)/(?P<VerticalId>[0-9a-zA-Z\-]+)$',
        views.CURDPublisherMedia),
    url(r'^CURDMediaLogo/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDMediaLogo),
    url(r'^CURDMediaKit/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDMediaKit),
    url(r'^DeleteMediakit/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.DeleteMediakit),

    url(r'^CURDMediaImage/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.MediaFileView.as_view()),
    url(r'^CURDMediaImage/(?P<pk>[0-9a-zA-Z\-]+)/(?P<ImageId>[0-9a-zA-Z\-]+)$',
        views.MediaFileView.as_view()),

    path('CURDMediaAdType/', views.CURDMediaAdTypeApi),
    path('CURDMediaAdTypeForDevApi/', views.CURDMediaAdTypeForDevApi),
    url(r'^CURDMediaAdType/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDMediaAdTypeApi),
    url(r'^uploadMediaAdType/$',
        views.MediaAdTypeFileView.as_view(), name='file-upload'),
    url(r'^uploadMediaAdType/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.MediaAdTypeFileView.as_view()),
    url(r'^CURDMediaAdTypeByMedia/(?P<MediaId>[0-9a-zA-Z\-]+)$',
        views.CURDMediaAdTypeByMediaApi),
    url(r'^CURDMediaAdTypeByMediaIdentification/(?P<MediaId>[0-9a-zA-Z\-]+)$',
        views.CURDMediaAdTypeByMediaIdentification),
    url(r'^DeleteAdUnitMediakit/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.DeleteAdUnitMediakit),


    path('CURDMediaAdTypeImage/', views.CURDMediaAdTypeImageApi),
    url(r'^CURDMediaAdTypeImage/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDMediaAdTypeImageApi),
    url(r'^uploadMediaAdTypeImage/$',
        views.MediaAdTypeImageFileView.as_view(), name='file-upload'),
    url(r'^uploadMediaAdTypeImage/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.MediaAdTypeImageFileView.as_view()),
    # path('CURDMediaImage/', views.CURDMediaImageAPi),
    url(r'^CURDMediaAdTypeImageByMedia/(?P<MediaId>[0-9a-zA-Z\-]+)$',
        views.CURDMediaAdTypeImageByMediaApi),
    url(r'^CURDMediaAdTypeImageByMediaIdentification/(?P<MediaId>[0-9a-zA-Z\-]+)$',
        views.CURDMediaAdTypeImageByMediaIdentification),




    path('RecommendedMediaByMedia/', views.RecommendedMediaByMedia),


    
    path('GetRecommendedAdUnit/', views.GetRecommendedAdUnit),
    path('GetRecommendedAdUnitByContryAudenc/', views.GetRecommendedAdUnitByContryAudenc),
    path('GetAllAdUnitForRecommendation/', views.GetAllAdUnitForRecommendation),

    
    path('CURDCountryByMediaAvailable/', views.CURDCountryByMediaAvailable),

     url(r'^GetAdunitData/(?P<count>[0-9a-zA-Z\-]+)$', views.GetAdunitData),
     path('RestMedia/', views.RestMedia),
     path('RestMediaAdType/', views.RestMediaAdType),
    
]
