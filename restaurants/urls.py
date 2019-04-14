from django.urls import path
from restaurants import views

urlpatterns = [
    path('restaurants/', views.restaurant_list),
    path('restaurants/<int:pk>/', views.restaurant_detail),
]