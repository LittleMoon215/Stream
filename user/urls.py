from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views
from user.views import RegisterView, MyObtainTokenPairView

urlpatterns = [
    path('register', views.RegisterView.as_view(), name="register_view"),
    path('login', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('streamkey', views.StreamKey.as_view())
]
