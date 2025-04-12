from django.urls import path, re_path as url
from app_default import views

urlpatterns = [
    path('userType/', views.UserTypeApi),
    path('Vertical/', views.VerticalApi),
    path('CURDVertical/', views.CURDVerticalApi),
    url(r'^Vertical/(?P<pk>[0-9a-zA-Z\-]+)$', views.VerticalApi),
    url(r'^uploadVertical/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.VerticalFileView.as_view()),
    path('CountryType/', views.CountryTypeApi),
    path('LightingType/', views.LightingTypeApi),
    path('VerticalStatus/', views.VerticalStatusApi),
    path('AdUnitCategory/', views.AdUnitCategoryApi),
    path('TimeZone/', views.TimeZoneApi),
    url(r'^TimeZone/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.TimeZoneApi),
    path('ServiceUnitType/', views.ServiceUnitTypeApi),
    path('ServiceOrderUnit/', views.ServiceOrderUnitApi),
    path('StaffPermission/', views.StaffPermissionApi),
    path('AdvertiserAssistanceSupport/', views.AdvertiserAssistanceSupportApi),
    path('OrganisationType/', views.OrganisationTypeApi),
    path('BotAavatar/', views.BotAavatarApi),

]
