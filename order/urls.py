from django.contrib import admin
from django.urls import path

from .views import GetAllOrder, GetOneOrder, SearchOrder, FilterOrder

urlpatterns = [
    path('order/all', GetAllOrder.as_view(), name='get_all_order'),
    path('order/<int:pk>', GetOneOrder.as_view(), name='get_one_order'),
    path('category/', FilterOrder.as_view(), name='filter_order'),
    path('order/', SearchOrder.as_view(), name='search_order'),
]
