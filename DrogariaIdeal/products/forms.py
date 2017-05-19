from django import forms
from django.forms import ModelForm
from .models import Product

class Create_Product_Form(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
