"""
URL configuration for GameSite project.

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
from django.urls import path
from gameapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', game_list, name='game_list'),           
    path('game/new/', game_create, name='game_create'), 
    path('game/<int:pk>/edit/', game_update, name='game_update'), 
    path('game/<int:pk>/delete/', game_delete, name='game_delete'), 
]
