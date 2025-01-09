from .models import *
from rest_framework import generics, permissions,authentication,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TVSerializer,CartSerializer,Cart_ItemsSerializer,ReviewSerializer,UserSerializer
from django.views.decorators.csrf import csrf_exempt


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]
    def put(self, request, pk, format=None):
        tv = self.get_object()
        serializer = TVSerializer(tv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        tv = self.get_object()
        tv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post (self, request, format=None):
        serializer = CartSerializer(data=request.data)
        serializer.initial_data['user'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def put(self, request, pk, format=None):
        cart = self.get_object()
        if cart.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        cart = self.get_object()
        if cart.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
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
        cart_item = self.get_object()
        if cart_item.cart.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = Cart_ItemsSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        cart_item = self.get_object()
        if cart_item.cart.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post(self, request, format=None):
        serializer = ReviewSerializer(data=request.data)
        serializer.initial_data['user'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def put(self, request, pk, format=None):
        review = self.get_object()
        if review.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        review = self.get_object()
        if review.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)