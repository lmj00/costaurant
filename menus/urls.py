from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('food/<int:pk>/', views.menu_detail)
]
