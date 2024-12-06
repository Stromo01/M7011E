from rest_framework import serializers
from models import TV,Cart,Cart_Items,Review

class TVSerializer(serializers.ModelSerializer):
    class Meta:
        model = TV
        fields = ['brand', 'model', 'price', 'resolution', 'tv_id', 'stock', 'screen_size']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user_id', 'cart_id', 'created_at']

class Cart_ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_Items
        fields = ['cart_item_id', 'cart_id']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['review_id', 'tv_id', 'user_id', 'rating', 'review']

