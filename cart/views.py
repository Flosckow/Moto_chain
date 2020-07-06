from django.shortcuts import render

from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from django.db.models import Sum

from cart.models import CartItem, Cart
from cart.serializers import CartItemSerializer

# Статус заказа Warning

# тест вьюхи и добавить урлы


class AddProductInCart(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartItemSerializer



# work
class AllCartItem(ListAPIView):
    cart_items = ''

    def get_queryset(self):
        self.cart_items = CartItem.objects.filter(cart__user=self.request.user)
        return self.cart_items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = Cart.objects.get(self.request.user).id
        context['price'] = self.cart_items.aggregate(Sum('sum_price'))

        return context
    serializer_class = CartItemSerializer


class EditCartItem(UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class DeleteCartItem(DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


