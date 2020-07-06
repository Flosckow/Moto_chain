from django.contrib import admin
from django.urls import path

from .views import GetAllUsers

urlpatterns = [
    path('all/', GetAllUsers.as_view(), name='get_all_users'),
]
