"""Views for the product app."""
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ProductList(generics.ListCreateAPIView):
    """View for listing and creating products."""

    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]

    def get_queryset(self):
        queryset = Product.objects.filter(
        ).only(
            'id',
            'name',
            'price',
            'category',
            'sub_category',
        )
        return queryset


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating and deleting products."""

    serializer_class = ProductSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]

    def get_queryset(self):
        queryset = Product.objects.filter(
        ).only(
            'id',
            'name',
            'price',
            'category',
            'sub_category',
            'brand',
            # 'description'
        )
        return queryset
