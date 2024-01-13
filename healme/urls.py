"""
URL configuration for healme project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import home,register,signin,signout,about,yoga,relaxing_music

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about',about,name="about"),
    path('relaxing_music',relaxing_music,name="relaxing_music"),
    path('yoga',yoga,name="yoga"),
    path('',home,name="home"),
    path('register',register,name="register"),
    path('login',signin,name="login"),
    path('logout',signout,name="logout"),
    path('chat/',include('chatbot.urls')),
    path('progress/',include('progress_tracking.urls')),

]
