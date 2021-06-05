"""djangoProject URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.urls import path, include
from rest_framework import serializers, viewsets, routers
from rest_framework_swagger.views import get_swagger_view

from Rent4Events import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'drivers', views.DriverViewSet)
router.register(r'order-positions',
                views.OrderPositionViewSet)
router.register(r'vehicles', views.VehicleViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'images', views.ImageViewSet)

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/public/', views.public),
    url(r'^api/private/', views.private),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rent-rest/', include('Rent4Events.urls')),
    url(r'^swagger/', schema_view),
    path('order-positions/<int:order_id>/<int:product_id>', views.OrderPositionViewSet.as_view({'get': 'retrieve',
                                                                                                'delete': 'destroy',
                                                                                                'patch': 'partial_update'}))

]
