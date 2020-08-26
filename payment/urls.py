from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from payment import views

urlpatterns = [
    path('simple-checkout/', views.simple_checkout, name='simple'),
    path('store/', views.store, name='store'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
    # path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
    # path('process-payment/', views.payment_process, name='process_payment'),
    # path('payment-done/', views.payment_done, name='payment_done'),
    # path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
]
