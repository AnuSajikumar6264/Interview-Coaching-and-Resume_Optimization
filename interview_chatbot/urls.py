from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='interview_chatbot_home'),
]
