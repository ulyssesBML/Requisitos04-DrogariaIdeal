from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from . import cart

def show_cart(request):
    user_id = request.user.id
    cart_products = cart.get_all_products(user_id)
    print (cart_products)

    return render(request, "show_cart/show_cart.html", {"cart_products":cart_products})

def remove_from_cart(request, product_id):
    user_id = request.user.id
    cart.remove_product(user_id, product_id)

    return HttpResponseRedirect(reverse('cart:show_cart'))
