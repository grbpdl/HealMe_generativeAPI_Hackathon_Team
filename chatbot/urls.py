from django.contrib import admin
from django.urls import path,include
from .views import handle_chat

urlpatterns = [
    path('',handle_chat,name="chat_handler"),
]
