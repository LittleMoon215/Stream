from django.contrib import admin
from django.urls import path
from . import views
import StreamPage.views

urlpatterns = [
    path('streams/', views.StreamsOnline.as_view()),
    path('streamname/', views.StreamName.as_view()),

]
