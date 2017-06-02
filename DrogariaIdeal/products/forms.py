# encoding: utf-8
from django import forms
from django.forms import ModelForm
from .models import Product, Category

class Create_Product_Form(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_name': 'Nome do Produto',
            'price': 'Preço',
            'factory_name': 'Fabricante',
            'bar_code': 'Codigo de Barra',
            'description': 'Descrição',
            'amount': 'Quantidade',
            'picture': 'Foto do Produto',
            'categories': 'Categoria',
            'featured':'Destaque',

        }

        widgets = {
            'categories': forms.CheckboxSelectMultiple()
        }


class Create_Category_Form(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'category_name': 'Nome da Categoria'
        }
