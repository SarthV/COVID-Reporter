from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('fillinfo', views.fillinfo, name =  'fillinfo'),
    path('listings', views.listings, name = 'listings')
]
