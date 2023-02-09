from django.contrib import admin
from django.urls import path,  include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('process', views.process, name="process"),
    path('social', views.social, name="social"),
]
