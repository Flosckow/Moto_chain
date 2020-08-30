from django.contrib import admin
from django.urls import path

from .views import GetAllUsers, GetUserForCart

urlpatterns = [
    path('all/', GetAllUsers.as_view(), name='get_all_users'),
    path('now-user/', GetUserForCart.as_view(), name='get_one_users'),
]
