from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.admin.views.decorators import staff_member_required

from .forms import Create_Product_Form, Create_Category_Form
from .models import Product, Category
from products.models import Product
from cart import cart
# Create your views here.



def search(request):
    query = request.GET.get('q')
    queryset_list = Product.objects.all()
    context = {
        'search_products': queryset_list.filter(product_name__icontains=query),
    }
    return render(request, 'listProducts/list_products_search.html', context)

@staff_member_required
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

@staff_member_required
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



@staff_member_required
def list_products(request):
    context = {
        'all_products': Product.objects.all(),
    }
    return render(request, 'listProducts/list_products.html', context)

@staff_member_required
def delete_products(request, product_id):
        Product.objects.get(id=product_id).delete()
        return HttpResponseRedirect(reverse('products:list_products'))

@staff_member_required
def create_category(request):

    if request.method == "POST":
        form = Create_Category_Form(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'createCategory/create_category.html', {'form': form, 'all_categories': Category.objects.all()})

    else:
        form = Create_Category_Form()
        return render(request, 'createCategory/create_category.html', {'form': form, 'all_categories': Category.objects.all()})

@staff_member_required
def delete_categories(request, category_id):
        Category.objects.get(id=category_id).delete()
        return HttpResponseRedirect(reverse('products:create_category'))

def sell_products(request):
    N_ELEMENTS = 15
    all_products = Product.objects.all()
    paginator = Paginator(all_products,N_ELEMENTS)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    context = {
        'all_products': products,
    }

    return render(request,"sellProducts/sell_products.html", context)

def add_to_cart(request, product_id):

    cart.add_product(request.user.id, product_id, 1)
    return HttpResponseRedirect(reverse('products:sell_products'))
