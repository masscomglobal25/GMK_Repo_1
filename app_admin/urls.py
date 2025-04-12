from django.urls import path, re_path as url
from app_admin import views

urlpatterns = [
    path('CURDMatchingCategory/', views.CURDMatchingCategoryApi),
    url(r'^CURDMatchingCategory/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDMatchingCategoryApi),
    url(r'^uploadMatchingCategory/$', views.MatchingCategoryFileView.as_view(), name='file-upload'),
    url(r'^uploadMatchingCategory/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.MatchingCategoryFileView.as_view()),


    path('CURDNationalityCommunity/', views.CURDNationalityCommunityApi),
    url(r'^CURDNationalityCommunity/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDNationalityCommunityApi),



    path('CURDIncomeGroup/', views.CURDIncomeGroupApi),
    url(r'^CURDIncomeGroup/(?P<pk>[0-9a-zA-Z\-]+)$', views.CURDIncomeGroupApi),
    url(r'^uploadIncomeGroup/$', views.IncomeGroupFileView.as_view(), name='file-upload'),
    url(r'^uploadIncomeGroup/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.IncomeGroupFileView.as_view()),


    path('CURDAgeGroup/', views.CURDAgeGroupApi),
    url(r'^CURDAgeGroup/(?P<pk>[0-9a-zA-Z\-]+)$', views.CURDAgeGroupApi),
    url(r'^uploadAgeGroup/$', views.AgeGroupFileView.as_view(), name='file-upload'),
    url(r'^uploadAgeGroup/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.AgeGroupFileView.as_view()),



    path('CURDGenderGroup/', views.CURDGenderGroupApi),
    url(r'^CURDGenderGroup/(?P<pk>[0-9a-zA-Z\-]+)$', views.CURDGenderGroupApi),
    url(r'^uploadGenderGroup/$', views.GenderGroupFileView.as_view(), name='file-upload'),
    url(r'^uploadGenderGroup/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.GenderGroupFileView.as_view()),


    path('CURDLocationType/', views.CURDLocationTypeApi),
    url(r'^CURDLocationType/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDLocationTypeApi),


    path('CURDEstimatedReach/', views.CURDEstimatedReachApi),
    url(r'^CURDEstimatedReach/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDEstimatedReachApi),



    path('CURDLanguage/', views.CURDLanguageApi),
    url(r'^CURDLanguage/(?P<pk>[0-9a-zA-Z\-]+)$', views.CURDLanguageApi),

    path('CURDAdBuzzTagging/', views.CURDAdBuzzTaggingApi),
    url(r'^CURDAdBuzzTagging/(?P<pk>[0-9a-zA-Z\-]+)$', views.CURDAdBuzzTaggingApi),



    path('CURDVerticalType/', views.CURDVerticalTypeApi),
    url(r'^CURDVerticalType/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDVerticalTypeApi),

    path('CURDContinentApi/', views.CURDContinentApi),
    url(r'^CURDContinentApi/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDContinentApi),


    path('CURDSEOCountryEventApi/', views.CURDSEOCountryEventApi),
    path('CURDCountryEventHomePage/', views.CURDCountryEventHomePage),
    path('CURDCountryEvent/', views.CURDCountryEventApi),
    url(r'^CURDCountryEvent/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDCountryEventApi),
    url(r'^uploadCountryEvent/$',
        views.CountryEventFileView.as_view(), name='file-upload'),
    url(r'^uploadCountryEvent/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CountryEventFileView.as_view()),
    url(r'^deleteCountryEventImage/(?P<FieldName>[0-9a-zA-Z\-]+)/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.DeleteCountryEventImage),



    path('CityRegionByCountry/', views.CityRegionByCountry),
    path('CURDCityRegion/', views.CURDCityRegionApi),
    url(r'^CURDCityRegion/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDCityRegionApi),
    # url(r'^CURDCityRegion/(?P<CountryEventId>[0-9a-zA-Z\-]+)$',
    #     views.CURDCityRegionApi),




    path('CURDNearByAdvantage/', views.CURDNearByAdvantageApi),
    url(r'^CURDNearByAdvantage/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDNearByAdvantageApi),
    url(r'^uploadNearByAdvantage/$',
        views.NearByAdvantageFileView.as_view(), name='file-upload'),
    url(r'^uploadNearByAdvantage/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.NearByAdvantageFileView.as_view()),




    path('CURDAdunitPosition/', views.CURDAdunitPositionApi),
    url(r'^CURDAdunitPosition/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDAdunitPositionApi),



    path('CURDAdunitSize/', views.CURDAdunitSizeApi),
    url(r'^CURDAdunitSize/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDAdunitSizeApi),



    path('CURDMediaCategory/', views.CURDMediaCategoryApi),
    url(r'^CURDMediaCategory/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDMediaCategoryApi),



    path('CURDAdFormat/', views.CURDAdFormatApi),
    url(r'^CURDAdFormat/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDAdFormatApi),

    path('CURDBrandCategory/', views.CURDBrandCategoryApi),
    url(r'^CURDBrandCategory/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDBrandCategoryApi),

    path('CURDCampaignObjective/', views.CURDCampaignObjectiveApi),
    url(r'^CURDCampaignObjective/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDCampaignObjectiveApi),




    path('CURDMeetingRequest/', views.CURDMeetingRequestApi),
    url(r'^CURDMeetingRequestByPublisher/(?P<PublisherId>[0-9a-zA-Z\-]+)$',
        views.CURDMeetingRequestApi),
    url(r'^CURDMeetingRequestByUser/(?P<UserType>[0-9a-zA-Z\-]+)$',
        views.CURDMeetingRequestByUser),
    url(r'^CURDMeetingRequest/(?P<PublisherId>[0-9a-zA-Z\-]+)/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDMeetingRequestApi),
    path('IsUserRequestedForMeeting/', views.IsUserRequestedForMeeting),



    path('CURDHelpRequiredFor/', views.CURDHelpRequiredForApi),
    url(r'^CURDHelpRequiredFor/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDHelpRequiredForApi),



    path('CURDAdUnitSpecificCategory/', views.CURDAdUnitSpecificCategoryApi),
    url(r'^CURDAdUnitSpecificCategory/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDAdUnitSpecificCategoryApi),
    url(r'^uploadAdUnitSpecificCategory/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.AdUnitSpecificCategoryFileView.as_view()),

    path('CURDHighlyRecommendedMedia/', views.CURDHighlyRecommendedMediaApi),
    url(r'^CURDHighlyRecommendedMedia/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDHighlyRecommendedMediaApi),
    url(r'^CURDHighlyRecommendedMediaByAudienceId/(?P<CountryId>[0-9a-zA-Z\-]+)/(?P<AudienceId>[0-9a-zA-Z\-]+)$',
        views.CURDHighlyRecommendedMediaByAudienceId),


    path('CURDRecommendationBanner/', views.CURDRecommendationBannerApi),
    url(r'^CURDRecommendationBanner/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDRecommendationBannerApi),
    url(r'^RecommendationBannerByAudienceId/(?P<CountryId>[0-9a-zA-Z\-]+)/(?P<AudienceId>[0-9a-zA-Z\-]+)$',
        views.CURDRecommendationBannerByAudienceId),
    url(r'^uploadRecommendationBanner/$',
        views.RecommendationBannerFileView.as_view(), name='file-upload'),
    url(r'^uploadRecommendationBanner/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.RecommendationBannerFileView.as_view()),



    path('CURDSiteBanner/', views.CURDSiteBannerApi),
    url(r'^CURDSiteBanner/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDSiteBannerApi),
    url(r'^CURDSiteBanner/(?P<CountryId>[0-9a-zA-Z\-]+)/(?P<AudienceId>[0-9a-zA-Z\-]+)/(?P<CategoryId>[0-9a-zA-Z\-]+)$',
        views.CURDSiteBanner),
    path('getSiteBannerMulti/', views.getSiteBannerMulti),
    url(r'^uploadSiteBanner/$',
        views.SiteBannerFileView.as_view(), name='file-upload'),
    url(r'^uploadSiteBanner/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.SiteBannerFileView.as_view()),


    path('CURDAdBuzzCategoryApi/', views.CURDAdBuzzCategoryApi),
    url(r'^CURDAdBuzzCategoryApi/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDAdBuzzCategoryApi),

    path('CURDCampaignUnit/', views.CURDCampaignUnitApi),
    url(r'^CURDCampaignUnit/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDCampaignUnitApi),
    url(r'^uploadCampaignUnit/$',
        views.CampaignUnitFileView.as_view(), name='file-upload'),
    url(r'^uploadCampaignUnit/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CampaignUnitFileView.as_view()),

        
    path('CURDSiteMenu/', views.CURDSiteMenuApi),
    url(r'^CURDSiteMenu/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDSiteMenuApi),
]

