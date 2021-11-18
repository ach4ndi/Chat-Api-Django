from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.urls import path, include, re_path

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
