from django.urls import path
from Rent4Events import views

urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail),
    path('groups/', views.group_list),
    path('api/public', views.public),
    path('api/private', views.private),
    path('api/private-scoped', views.private_scoped),
    # path('groups/<int:pk>/', views.user_detail),
]