from django.urls import path, re_path as url
from app_credit import views

urlpatterns = [
    path('Credits/', views.CreditsApi),
    path('CreditRequired/', views.CURDCreditRequiredApi),
    url(r'^CreditRequired/(?P<pk>[0-9a-zA-Z\-]+)$',
        views.CURDCreditRequiredApi),
    url(r'^HasCreditRequestAdvertiser/(?P<UserId>[0-9a-zA-Z\-]+)$',
        views.HasCreditRequestAdvertiser),
]
