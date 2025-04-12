

from django.urls import path, re_path as url
from app_chat_gpt import views


urlpatterns = [
    path('gpt-content-changer/', views.ConvertContentWithPrompt),
    path('test-gpt-content-changer/', views.TestConvertContentWithPrompt),
    path('GenerateAiPlan/', views.GenerateAiPlan),

]
