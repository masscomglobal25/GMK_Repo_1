from django.urls import path, re_path as url
from app_site import views

urlpatterns = [
    path('CURDLog/', views.CURDLogApi),
    url(r'^CURDLog/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDLogApi),
    path('CURDSiteSettings/', views.CURDSiteSettingsApi),
    url(r'^CURDSiteSettings/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDSiteSettingsApi),
    path('SaveForPDFDownload/', views.CURDCampaignPDFDataApi),
    url(r'^DeletePDFDownload/(?P<UserId>[0-9a-zA-Z\-]+)/(?P<CampaignId>[0-9a-zA-Z\-]+)$',
        views.CURDCampaignPDFDataApi),

    path('SiteDetail/', views.SiteDetail),
    path('WebStats/', views.WebStatsAPI),
    
    url(r'^CalenderHoliday/(?P<CountryCode>[0-9a-zA-Z\-]+)/(?P<Year>[0-9a-zA-Z\-]+)$',
        views.CalenderHolidayAPI),

    path('CURDComments/', views.CURDCommentsApi),
    url(r'^CURDComments/(?P<CommentType>[0-9a-zA-Z\-]+)/(?P<TypeId>[0-9a-zA-Z\-]+)$',
        views.CURDCommentsApi),

    path('LinkedInAuth/', views.LinkedInAuth),
    # path('renameFiles/', views.renameFiles),
    path('CURDPriorityCodeApi/', views.CURDPriorityCodeApi),
    url(r'^CURDPriorityCodeApi/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDPriorityCodeApi),
    url(r'^CURDCheckPriorityCodeApi/(?P<Code>[0-9a-zA-Z\-]+)$',
        views.CURDCheckPriorityCodeApi),
]
