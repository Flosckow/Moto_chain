from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from .models import MotoUser
from .serializers import MotoUserSerialazers


class GetAllUsers(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = MotoUser.objects.filter(is_active=True).order_by('-date_joined')
    serializer_class = MotoUserSerialazers
