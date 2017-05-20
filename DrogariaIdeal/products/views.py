from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import Create_Product_Form
from .models import Product
# Create your views here.


def create_product(request):
    if request.method == "POST":
        form = Create_Product_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('products:list_products'))
        return render(request, 'create_product.html', {'form': form})

    else:
        form = Create_Product_Form()
        return render(request, 'create_product.html', {'form': form})


def list_products(request):
    context = {
        'all_products': Product.objects.all(),
    }
    return render(request, 'list_products.html', context)

def delete_products(request, product_id):
        Product.objects.get(id=product_id).delete()
        return HttpResponseRedirect(reverse('products:list_products'))
