from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
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
router.register(r'available', views.AvailableProductsView, basename="AvailableProducts")
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^swagger/', schema_view),
    # path('users/', views.user_list),
    # path('users/<int:pk>/', views.user_detail),
    # path('groups/', views.group_list),
    path('api/public', views.public),
    path('api/private', views.private),
    path('api/private-scoped', views.private_scoped),

    path('', include(router.urls)),
    path('order-positions/<int:order_id>/<int:product_id>', views.OrderPositionViewSet.as_view({'get': 'retrieve',
                                                                                                'delete': 'destroy',
                                                                                                'patch': 'partial_update'}))
    # path('groups/<int:pk>/', views.user_detail),
]