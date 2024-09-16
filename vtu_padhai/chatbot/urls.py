# chatbot/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chatbot, name='chatbot'),
]
# chatbot/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_interface, name='chatbot_interface'),
    path('chat/', views.chatbot, name='chatbot'),
]
