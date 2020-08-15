from django.views.generic.base import View
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated

from cart.models import CartItem, Cart, OrderProduct
from cart.serializers import CartItemSerializer, OrderProductSerializer, CreateCartItemSerializer, \
    DeleteCartItemSerializer


class AddProductInCart(CreateAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = CreateCartItemSerializer

    def perform_create(self, serializer):
        serializer.save(cart=Cart.objects.get(user=self.request.user))


class AllCartItem(ListAPIView):
    permission_classes = [IsAuthenticated]
    cart_items = ''

    def get_queryset(self):
        print(self.request.user.id)
        self.cart_items = CartItem.objects.filter(cart__user=self.request.user) # ошибка тут, смотреть модели
        return self.cart_items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = Cart.objects.get(self.request.user).id
        context['price'] = self.cart_items.aggregate(Sum('sum_price'))

        return context
    serializer_class = CartItemSerializer


class EditCartItem(UpdateAPIView):
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        self.cart_items = CartItem.objects.filter(cart__user=self.request.user)
        return self.cart_items
    serializer_class = CartItemSerializer


class DeleteCartItem(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        self.cart_items = CartItem.objects.get(cart= self.request.user)
        return self.cart_items

    serializer_class = DeleteCartItemSerializer




class AddOrder(CreateAPIView):
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        self.order = OrderProduct.objects.filter(cart__user=self.request.user)
        return self.order
    serializer_class = OrderProductSerializer


class OrderList(ListAPIView):
    # permission_classes = [IsAuthenticated]
    """Список заказов пользователя"""
    # template_name = "shop/order-list.html"
    order = ''

    def get_queryset(self):
        self.order = OrderProduct.objects.filter(cart__user=self.request.user)
        return self.order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total"] = self.order.aggregate(Sum('cart__cart_item__sum_price'))
        return context

    serializer_class = OrderProductSerializer


# рефактор удаления заказа
class DeleteOrderProduct(DestroyAPIView):
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        self.order = OrderProduct.objects.filter(cart__user=self.request.user)
        return self.order


    serializer_class = OrderProductSerializer






