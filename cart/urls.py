from django.contrib import admin
from django.urls import path

from .views import AllCartItem, AddProductInCart, DeleteCartItem, EditCartItem

urlpatterns = [
    path("add-cart-item/<int:pk>/", AddProductInCart.as_view(), name="add_cart_item"),
    path("cart/", AllCartItem.as_view(), name="all_cart_item"),
    path("delete/<int:pk>/", DeleteCartItem.as_view(), name="del_item"),
    path("edit/<int:pk>/", EditCartItem.as_view(), name="edit_item"),
]
