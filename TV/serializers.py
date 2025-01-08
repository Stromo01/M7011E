from rest_framework import serializers
from .models import TV,Cart,Cart_Items,Review
from django.contrib.auth.models import User

class TVSerializer(serializers.ModelSerializer):
    class Meta:
        model = TV
        fields = ['brand', 'model', 'price', 'resolution', 'tv_id', 'stock', 'screen_size']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'cart_id', 'created_at']

class Cart_ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_Items
        fields = ['cart_item_id', 'cart', 'tv', 'quantity']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['review_id', 'tv', 'user', 'rating', 'review_text']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

