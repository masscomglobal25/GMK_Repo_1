from django.urls import path, re_path as url
from app_page_seo import views


urlpatterns = [
    path('CURDPageSeo/', views.CURDPageSeoApi),
    url(r'^CURDPageSeo/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDPageSeoApi),
    path('CURDBoutiquePageSeo/', views.CURDBoutiquePageSeoApi),
    url(r'^CURDBoutiquePageSeo/(?P<CountryId>[0-9a-zA-Z\-]+)/(?P<AudienceId>[0-9a-zA-Z\-]+)$',
        views.CURDBoutiquePageSeoApi),
    # path('CURDPageForSeo/', views.CURDPageForSeoApi),
]