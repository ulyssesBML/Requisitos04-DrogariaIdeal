# encoding: utf-8
from django import forms
from django.forms import ModelForm
from .models import Product

class Create_Product_Form(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_name': 'Nome do Produto',
            'price': 'preço',
            'factory_name': 'Fabricante',
            'bar_code': 'Codigo de Barra',
            'description': 'Descrição',
            'amount': 'quantidade',
            'picture': 'Foto do Produto',

        }
