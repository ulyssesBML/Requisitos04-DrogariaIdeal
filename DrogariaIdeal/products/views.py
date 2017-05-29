from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import Create_Product_Form, Create_Category_Form
from .models import Product, Category
from products.models import Product
# Create your views here.



def search(request):
    query = request.GET.get('q')
    queryset_list = Product.objects.all()
    context = {
        'search_products': queryset_list.filter(product_name__icontains=query),
    }
    return render(request, 'listProducts/list_products_search.html', context)

def create_product(request):
    if request.method == "POST":
        form = Create_Product_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('products:list_products'))
        return render(request, 'createProduct/create_product.html', {'form': form})

    else:
        form = Create_Product_Form()
        return render(request, 'createProduct/create_product.html', {'form': form})

def edit_product(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = Create_Product_Form(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('products:list_products'))
        return render(request, 'editProduct/edit_products.html', {'form': form})

    else:
        form = Create_Product_Form(instance=product)
        return render(request, 'editProduct/edit_products.html', {'form': form})



def list_products(request):
    context = {
        'all_products': Product.objects.all(),
    }
    return render(request, 'listProducts/list_products.html', context)

def delete_products(request, product_id):
        Product.objects.get(id=product_id).delete()
        return HttpResponseRedirect(reverse('products:list_products'))

def create_category(request):

    if request.method == "POST":
        form = Create_Category_Form(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'createCategory/create_category.html', {'form': form, 'all_categories': Category.objects.all()})

    else:
        form = Create_Category_Form()
        return render(request, 'createCategory/create_category.html', {'form': form, 'all_categories': Category.objects.all()})

def delete_categories(request, category_id):
        Category.objects.get(id=category_id).delete()
        return HttpResponseRedirect(reverse('products:create_category'))
