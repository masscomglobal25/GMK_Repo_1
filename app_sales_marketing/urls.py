from django.urls import path, re_path as url
from app_sales_marketing import views


urlpatterns = [
    
    path('CURDSalesMarketing/', views.CURDSalesMarketingApi),
    url(r'^CURDSalesMarketing/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDSalesMarketingApi),
    path('CURDSalesMarketingDetail/', views.CURDSalesMarketingDetailApi),
    url(r'^CURDSalesMarketingDetail/(?P<SalesMarketingId>[0-9a-zA-Z\-]+)$',
        views.CURDSalesMarketingDetailApi),
    url(r'^CURDSalesMarketingDetail/(?P<SalesMarketingId>[0-9a-zA-Z\-]+)/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDSalesMarketingDetailApi),
]