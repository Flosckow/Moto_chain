from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'title', 'image', 'price', 'description', 'category']


