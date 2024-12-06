from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tvs/', views.TVListView.as_view(), name='tvs'),
    path('tv/<int:pk>', views.TVDetailView.as_view(), name='tv-detail'),
    path('cart/', views.CartListView.as_view(), name='cart'),
    path('review/', views.ReviewListView.as_view(), name='review'),

]