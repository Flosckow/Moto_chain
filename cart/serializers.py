from rest_framework import serializers

from .models import CartItem, OrderProduct


class CreateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'sum_price', ]


class DeleteCartItemSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'sum_price']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cart', 'product', 'quantity', 'sum_price']


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['cart', 'status', 'is_active', 'date']
