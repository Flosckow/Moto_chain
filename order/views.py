from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import filters
from .models import Order
from .serializers import OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


class GetAllOrder(ListAPIView):
    queryset = Order.objects.all().order_by('title')
    serializer_class = OrderSerializer


class GetOneOrder(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'order_len'
    max_page_size = 30


class FilterOrder(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'price']


class SearchOrder(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
