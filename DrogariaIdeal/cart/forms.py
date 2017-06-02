# encoding: utf-8
from django import forms
from django.forms import ModelForm
from .models import Order


class Create_Order_Form(ModelForm):
    class Meta:
        model = Order
        fields = {
            'payment',
            'flag',
            'change'
        }
        labels = {
            'payment': 'forma de pagamento',
            'flag': 'bandeira',
            'change': 'troco'
        }
