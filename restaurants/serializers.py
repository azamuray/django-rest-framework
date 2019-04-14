from rest_framework import serializers
from restaurants.models import Restaurant, Product, LANGUAGE_CHOICES, STYLE_CHOICES


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'title', 'longitude', 'latitude')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category', 'image')