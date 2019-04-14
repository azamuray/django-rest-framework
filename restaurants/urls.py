from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from restaurants import views

urlpatterns = [
    path('restaurants/', views.restaurant_list),
    path('restaurants/<int:pk>/', views.restaurant_detail),
    path('products/', views.product_list),
    path('products/<int:pk>/', views.product_detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)