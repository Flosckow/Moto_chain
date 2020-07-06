from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        category = serializers.SlugRelatedField(slug_field="title", read_only=True)
        fields = ['id', 'title', 'image', 'price', 'description', 'category']


