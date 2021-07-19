from django.contrib import admin
from django.urls import path
from . import views
import streampage.views

urlpatterns = [
    path('', views.index, name="index"),
]
