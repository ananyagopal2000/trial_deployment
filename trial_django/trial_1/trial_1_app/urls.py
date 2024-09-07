from django.shortcuts import redirect
from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('', views.home, name = 'home'),
]