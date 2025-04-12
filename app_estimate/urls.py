

from django.urls import path, re_path as url
from app_estimate import views


urlpatterns = [
	path('', views.index),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    url(r'^pdf_download/(?P<PlanId>[0-9a-zA-Z\-]+)/(?P<UserId>[0-9a-zA-Z\-]+)$',views.DownloadPDF.as_view(), name="pdf_download"),
]
