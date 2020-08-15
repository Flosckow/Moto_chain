from datetime import datetime

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from moto_user.models import MotoUser
from order.models import Order


class Cart(models.Model):
    user = models.ForeignKey(MotoUser, on_delete=models.CASCADE, related_name='user_cart')
    is_active = True
    is_order = False


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')  # change field on_delete
    quantity = models.PositiveIntegerField('Количество', default=1)
    sum_price = models.PositiveIntegerField('Общая цена', default=0)


    def save(self, *args, **kwargs):
        self.sum_price = self.quantity * self.product.price
        super().save(*args, **kwargs)


class OrderProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField('Статус заказа', max_length=25, default='В обработке')
    is_active = False
    date = models.DateTimeField('Дата', default=datetime.now())


@receiver(post_save, sender=MotoUser)
def create_user_cart(sender, instance, created, **kwargs):
    """Создание корзины пользователя"""
    if created:
        Cart.objects.create(user=instance)