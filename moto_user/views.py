from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from cart.models import Cart
from .models import MotoUser
from .serializers import MotoUserSerialazers


class GetAllUsers(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = MotoUser.objects.filter(is_active=True).order_by('-date_joined')
    serializer_class = MotoUserSerialazers


class GetUserForCart(ListAPIView):
    # permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    serializer_class = MotoUserSerialazers
