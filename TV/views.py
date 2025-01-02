from .models import *
from rest_framework import generics, permissions,authentication,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TVSerializer,CartSerializer,Cart_ItemsSerializer,ReviewSerializer


class TVList(generics.ListCreateAPIView):
    queryset = TV.objects.all()
    serializer_class = TVSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post(self, request, format=None):
        serializer = TVSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TVDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TV.objects.all()
    serializer_class = TVSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def put(self, request, pk, format=None):
        tv = self.get_object(pk)
        serializer = TVSerializer(tv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        tv = self.get_object(pk)
        tv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post (self, request, format=None):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def put(self, request, pk, format=None):
        cart = self.get_object(pk)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        cart = self.get_object(pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CartItemsList(generics.ListCreateAPIView):
    queryset = Cart_Items.objects.all()
    serializer_class = Cart_ItemsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post(self, request, format=None):
        serializer = Cart_ItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart_Items.objects.all()
    serializer_class = Cart_ItemsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def put(self, request, pk, format=None):
        cart_item = self.get_object(pk)
        serializer = Cart_ItemsSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        cart_item = self.get_object(pk)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post(self, request, format=None):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def put(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
