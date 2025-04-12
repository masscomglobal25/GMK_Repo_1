from django.urls import path, re_path as url
from app_ai_external import views

urlpatterns = [
    path('GetTagCountries/', views.GetTagCountries),
    path('CountryEvent/', views.CountryEventApi),
    path('CityRegion/', views.CityRegionApi),
    path('GetTagDetailsByCountry/', views.GetTagDetailsByCountry),
    url(r'^GetTagDetailsByCountry/(?P<CountryEventId>[0-9a-zA-Z\-]+)$',
        views.GetTagDetailsByCountry),
        
    path('CURDAIFilteredData/', views.CURDAIFilteredDataApi),
    path('MediaAdTypeWithMediaView/', views.mediaAdTypeWithMediaView),
    url(r'^CURDAIFilteredData/(?P<UserId>[0-9a-zA-Z\-]+)$',
        views.CURDAIFilteredDataApi),
    url(r'^MediaFromAI/(?P<UserId>[0-9a-zA-Z\-]+)$',
        views.MediaFromAIApi),
    
    path("download_filtered_data_as_excel/", views.get_filtered_data, name="download_excel"),
]
