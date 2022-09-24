"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from service.views import *
from rest_framework import routers


router_cat = routers.SimpleRouter()
router_cat.register(r'cat', CatViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', UserAPIList.as_view()),
    path('api/v1/users/<int:pk>/', UserAPIUpdate.as_view()),
    path('api/v1/userdelete/<int:pk>/', UserAPIDestroy.as_view()),
    path('api/v1/cats/', include(router_cat.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
