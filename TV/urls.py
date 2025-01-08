from django.urls import path
from . import views

urlpatterns = [
    path('create-user/',views.create_user, name='create-user'),
    path('tvs/', views.TVList.as_view(), name='tv-list'),
    path('tvs/<int:pk>/', views.TVDetail.as_view(), name='tv-detail'),
    path('carts/', views.CartList.as_view(), name='cart-list'),
    path('carts/<int:pk>/', views.CartDetail.as_view(), name='cart-detail'),
    path('cart-items/', views.CartItemsList.as_view(), name='cart-items-list'),
    path('cart-items/<int:pk>/', views.CartItemsDetail.as_view(), name='cart-items-detail'),
    path('reviews/', views.ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
]