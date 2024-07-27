"""Serializer for Product model."""

from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model."""

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "category",
            "sub_category",
        ]
        read_only_fields = ["id"]
