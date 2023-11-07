"""quotesapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import serializers, generics
from quotes.models import Product, Section
from rest_framework import routers, serializers, viewsets
from rest_framework.routers import DefaultRouter
from quotes.views import main
from quotes.views import ProductViewSet, SectionViewSet

# Crea un enrutador
router = DefaultRouter()
# Registra las vistas con el enrutador
router.register(r'products', ProductViewSet)
router.register(r'sections', SectionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]


