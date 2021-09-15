from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('get-users/', views.get_users, name='get-users'),
    path('get-accounts/', views.get_accounts, name='get-accounts'),
    path('get-contacts/', views.get_contacts, name='get-contacts'),
]
