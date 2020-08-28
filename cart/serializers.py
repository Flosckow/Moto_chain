from rest_framework import serializers

from .models import CartItem, OrderProduct
from order.models import Order

class CreateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'sum_price']


class DeleteCartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'sum_price']


class ProductImgSer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('image', 'title')


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductImgSer()

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity', 'sum_price']


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['cart', 'status', 'is_active', 'date']

