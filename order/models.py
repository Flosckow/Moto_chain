from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    tagline = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Order(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    image = models.ImageField(default=None, upload_to='order/media')
    price = models.DecimalField(max_digits=19, decimal_places=10)
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='orders')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

