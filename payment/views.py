import json
from audioop import reverse

from django.shortcuts import render, get_object_or_404

# оплата товара с помощью пайпал
from django.views.decorators.csrf import csrf_exempt
# сделать по видео)
from paypal.standard.forms import PayPalPaymentsForm

from cart.models import OrderProduct, CartItem
from moto_shop import settings


def simple_checkout(request):

    return render(request, 'moto_shop/simple_checkout.html')


def store(request):
    orders = CartItem.objects.all()
    context = {'orders': orders}
    return render(request, 'moto_shop/store.html', context)

def checkout(request):
    orders = CartItem.objects.all()
    context = {'orders': orders}
    return render(request, 'moto_shop/checkout.html', context)

def payment_complete(request):  # исправить этот метод, при успешной оплате создает заказ
    body = json.loads(request.body)
    print(body)
    orders = CartItem.objects.get(id=body['orders.id'])
    OrderProduct.create(
        cart=orders.cart

    )



























# @csrf_exempt
# def payment_process(request):
#     order_id = request.session.get('OrderProduct_id')
#     print(order_id)
#     order = get_object_or_404(OrderProduct, id=order_id) # ошибка вот тут No OrderProduct matches the given query.
#     host = request.get_host()
#     paypal_dict = {
#         'business': settings.PAYPAL_RECEIVER_EMAIL,
#         'amount': f"{OrderProduct.sum_price}",  # Изменить на order product, если не будет работать
#         'item_name': 'Order ' + f"{order_id}",
#         'currency_code': 'USD',
#         'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
#         'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
#         'cancel_return': 'http://{}{}'.format(host, reverse('payment_canceled')),
#     }
#     form = PayPalPaymentsForm(initial=paypal_dict)
#     return render(request, 'moto_shop/process_payment.html', {'order': order, 'form': form}) # возвращает OKAY, значит работает?
#
#
# @csrf_exempt
# def payment_done(request):
#     return render(request, 'moto_shop/payment_done.html')
#
#
# @csrf_exempt
# def payment_cancelled(request):
#     return render(request, 'moto_shop/payment_cancelled.html')
#
