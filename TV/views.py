from .models import *
from rest_framework import generics, permissions,authentication,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TVSerializer,CartSerializer,Cart_ItemsSerializer,ReviewSerializer


class TVList(generics.ListCreateAPIView):
    queryset = TV.objects.all()
    serializer_class = TVSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   # authentication_classes = [authentication.TokenAuthentication]


class TVDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TV.objects.all()
    serializer_class = TVSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #authentication_classes = [authentication.TokenAuthentication]
    def post(self, request, format=None):
        serializer = TVSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
    authentication_classes = [authentication.TokenAuthentication]

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]

class CartItemsList(generics.ListCreateAPIView):
    queryset = Cart_Items.objects.all()
    serializer_class = Cart_ItemsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]

class CartItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart_Items.objects.all()
    serializer_class = Cart_ItemsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]
