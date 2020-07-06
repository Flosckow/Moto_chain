from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import MotoUser
from .serializers import MotoUserSerialazers


class GetAllUsers(ListAPIView):
    queryset = MotoUser.objects.filter(is_active=True).order_by('-date_joined')
    serializer_class = MotoUserSerialazers
