from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import AllCartItem, AddProductInCart, DeleteCartItem, EditCartItem, OrderList, AddOrder, DeleteOrderProduct

urlpatterns = [
    path("add-cart-item/<int:pk>/", AddProductInCart.as_view(), name="add_cart_item"),
    path("cart/", AllCartItem.as_view(), name="all_cart_item"),
    path("delete/<int:pk>/", DeleteCartItem.as_view(), name="del_item"),
    path("edit/<int:pk>/", EditCartItem.as_view(), name="edit_item"),
    path("add-order", csrf_exempt(AddOrder.as_view()), name="add_order"),
    path('orders/', csrf_exempt(OrderList.as_view()), name='all_orders'),
    path('order/delete/<int:pk>/', csrf_exempt(DeleteOrderProduct.as_view()), name='delete_orders'),
]
