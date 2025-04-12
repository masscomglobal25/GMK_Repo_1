from django.urls import path, re_path as url
from app_invoice import views

urlpatterns = [
    path('downloadInvoice/', views.ViewPDF.as_view(), name='downloadInvoice'),
]