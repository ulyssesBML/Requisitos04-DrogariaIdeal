# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from products.models import Product
from users.models import CustomUser

class ProductOrder(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField()
    def __str__(self):
        return self.product.product_name



class Order(models.Model):
    PAYMENT = (
        ('Credito', 'Cartão de Credito'),
        ('Debito', 'Cartão de Debito'),
        ('Dinheiro', 'Dinheiro'),
    )
    payment = models.CharField(
        max_length=9,
        choices=PAYMENT,
        default='Dinheiro',
    )
    FLAG = (
        ('', ''),
        ('Visa', 'Visa'),
        ('MasterCard', 'MasterCard'),
        ('AmericanExpress', 'AmericanExpress'),
    )
    flag = models.CharField(
        max_length=16,
        choices=FLAG,
        default='',
        blank=True,
    )
    change = models.DecimalField(max_digits=8, decimal_places=2,default=0,blank=True)
    orders = models.ManyToManyField(ProductOrder)
    total_price = models.IntegerField(null=False)
    user = models.IntegerField()

    STATE = (
        ('pending', 'Pendente'),
        ('delivered', 'Entregue'),
        ('cancelled', 'Cancelado'),
    )
    state = models.CharField(
        max_length=16,
        choices=STATE,
        default='pending',
    )
