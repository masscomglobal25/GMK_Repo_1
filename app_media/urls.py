from django.urls import path, re_path as url
from app_media import views


urlpatterns = [
    path('CURDCart/', views.CURDCartApi),
    # url(r'^CURDCart/(?P<userId>[0-9a-zA-Z\-]+)$',
    #     views.CURDCartApi),
    # url(r'^CURDCart/(?P<userId>[0-9a-zA-Z\-]+)/(?P<pk>[0-9a-zA-Z\-]+)$',
    #     views.CURDCartApi),
    url(r'^CURDCart/(?P<userId>[0-9a-zA-Z\-]+)/(?P<CartType>[0-9a-zA-Z\-]+)$',
        views.CURDCartApi),
    url(r'^CURDCart/(?P<userId>[0-9a-zA-Z\-]+)/(?P<CartType>[0-9a-zA-Z\-]+)/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDCartApi),


    url(r'^CURDCartRecommendedMedia/(?P<userId>[0-9a-zA-Z\-]+)/(?P<CartType>[0-9a-zA-Z\-]+)$',
        views.CURDCartRecommendedMediaApi),


    path('CURDPlan/', views.CURDPlanApi),
    url(r'^CURDPlan/(?P<userId>[0-9a-zA-Z\-]+)$',
        views.CURDPlanApi),
    url(r'^CURDPlan/(?P<userId>[0-9a-zA-Z\-]+)/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDPlanApi),

    url(r'^CURDPlanByAdmin/',
        views.CURDPlanByAdmin),
    url(r'^CURDPlanByPublisher/(?P<userId>[0-9a-zA-Z\-]+)$',
        views.CURDPlanByPublisher),

    path('CURDPlanDetail/', views.CURDPlanDetailApi),
    url(r'^CURDPlanDetail/(?P<planId>[0-9a-zA-Z\-]+)/(?P<AdvertiserId>[0-9a-zA-Z\-]+)/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDPlanDetailApi),
    url(r'^CURDPlanDetail/(?P<planId>[0-9a-zA-Z\-]+)/(?P<AdvertiserId>[0-9a-zA-Z\-]+)$',
        views.CURDPlanDetailApi),
    url(r'^CURDPlanDetail/(?P<planId>[0-9a-zA-Z\-]+)$',
        views.CURDPlanDetailApi),

    url(r'^CURDPlanDetailByPublisher/(?P<userId>[0-9a-zA-Z\-]+)$',
        views.CURDPlanDetailByPublisher),
    url(r'^CURDPlanDetailByPublisher/(?P<userId>[0-9a-zA-Z\-]+)/(?P<planId>[0-9a-zA-Z\-]+)$',
        views.CURDPlanDetailByPublisher),
    url(r'^CURDPlanDetailByAdmin/',
        views.CURDPlanDetailByAdmin),



    path('CURDPlanEstimateShorten/', views.CURDPlanEstimateShortenApi),
    url(r'^CURDPlanEstimateShorten/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDPlanEstimateShortenApi),
    url(r'^CURDPlanEstimateShorten/(?P<PlanId>[0-9a-zA-Z\-]+)/(?P<UserId>[0-9a-zA-Z\-]+)$',
        views.PlanEstimateShortenApi),




    url(r'^DashboardDataForPublisher/(?P<PublisherId>[0-9a-zA-Z\-]+)$',
        views.dashboardDataForPublisher),
    url(r'^DashboardDataForAdvertiser/(?P<AdvertiserId>[0-9a-zA-Z\-]+)$',
        views.dashboardDataForAdvertiser),


    url(r'^publisherPlanDetails/(?P<PublisherId>[0-9a-zA-Z\-]+)$',
        views.publisherPlanDetails),
    url(r'^advertiserPlanDetails/(?P<AdvertiserId>[0-9a-zA-Z\-]+)$',
        views.advertiserPlanDetails),
    url(r'^allPlanDetails/',
        views.allPlanDetails),


    
    
    path('CURDCampaignReportRegister/', views.CURDCampaignReportRegisterApi),
    url(r'^CURDCampaignReportRegister/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDCampaignReportRegisterApi),
    path('CURDCampaignReportDetail/', views.CURDCampaignReportDetailApi),
    url(r'^CURDCampaignReportDetail/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDCampaignReportDetailApi),
    url(r'^uploadCampaignReportRegister/$',
        views.CampaignReportRegisterFileView.as_view(), name='file-upload'),
    url(r'^uploadCampaignReportRegister/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CampaignReportRegisterFileView.as_view()),
    url(r'^CampaignReport/(?P<PlanDetailId>[0-9a-zA-Z\-]+)/(?P<PlanId>[0-9a-zA-Z\-]+)$',
        views.CampaignReport),
]
