from django.urls import path
from Rent4Events import views

urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail),
    path('groups/', views.group_list),
    # path('groups/<int:pk>/', views.user_detail),
]