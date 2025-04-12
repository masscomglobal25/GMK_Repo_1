from django.urls import path, re_path as url
from app_login import views

urlpatterns = [
    path('login/', views.loginApi),
    path('UpdateGMKUserPassword/', views.loginApi),
    path('CheckEmailRestPassword/', views.CheckEmailRestPasswordApi),
    path('CheckEmail/', views.CheckEmailApi),
    path('CreateloginApi/', views.CreateloginApi),
    url(r'^login/(?P<pk>[0-9a-zA-Z\-]+)$', views.loginApi),
    url(r'^GetLoginByLoginId/(?P<LoginId>[0-9a-zA-Z\-]+)$', views.GetLoginByLoginIdApi),
    path('loginStatus/', views.loginStatusApi),
    url(r'^GetLogin/(?P<UserId>[0-9a-zA-Z\-]+)$', views.GetLoginApi),
    path('AdvertiserSocialLogin/', views.AdvertiserSocialLoginApi),
    path('PublisherSocialLogin/', views.PublisherSocialLoginApi),
    url(r'^UserToken/(?P<TokenId>[0-9a-zA-Z\-]+)$', views.UserTokenApi),
]
