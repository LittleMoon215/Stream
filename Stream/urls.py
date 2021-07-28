from django.contrib import admin
from django.urls import path, include
from StreamPage import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("user.urls")),
    path('', views.index, name="index"),
    path('api/', include("StreamPage.urls")),
]
