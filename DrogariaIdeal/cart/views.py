import sys
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from . import cart
from .forms import Create_Order_Form
from .models import Order, ProductOrder
from users.models import CustomUser

def show_cart(request):
    context = {}
    user_id = request.user.id
    cart_products = cart.get_all_products(user_id)
    amount = []

    context["cart_products"] = cart_products

    if request.method == "POST":
        form = request.POST
        order_form = Create_Order_Form(request.POST)
        if order_form.is_valid:
            order_form.instance.user = CustomUser.objects.get(id=request.user.id).id
            order_form.instance.total_price = 0
            order_form.save()
            for i,product in enumerate(cart_products):
               amount.append(form.get("amount" + str(i+1)))
               product_O = ProductOrder(product.id, amount[i])
               product_O.product = product
               product_O.amount = amount[i]
               product_O.save()
               order_form.instance.orders.add(product_O.id)

            order_form.instance.total_price = total_price(cart_products, amount)
            order_form.save()

            cart.clear(user_id)

            url = reverse('cart:list_products_order', kwargs={"order_id":order_form.instance.id})

            return HttpResponseRedirect(url)

        return render(request, "show_cart/show_cart.html", context)

    else:
        order_form = Create_Order_Form()
        context["form"] = order_form
        return render(request, "show_cart/show_cart.html", context)


def remove_from_cart(request, product_id):
    user_id = request.user.id
    cart.remove_product(user_id, product_id)

    return HttpResponseRedirect(reverse('cart:show_cart'))


def total_price(cart_products, amount):
    price = 0
    print(len(cart_products))
    print(len(amount))
    for product_num in range(0, len(cart_products)):
        price = price + float(cart_products[product_num].price)*float(amount[product_num])
    return price


def list_orders(request):
    context = {}
    context['all_orders'] = Order.objects.all()

    return render(request,"listOrders/list_orders.html", context)


def list_products_order(request,order_id):
    context = {}
    products = []
    amount = []
    main_order = Order.objects.get(id=order_id)
    context["client"] = CustomUser.objects.get(id= main_order.user)
    context["total_price"] = main_order.total_price
    context['order'] = main_order.orders.all()
    return render(request,"listProductsOrder/list_products_order.html", context)


def cancel_order(request, order_id):
    order = Order.objects.get(id = order_id).delete()
    return HttpResponseRedirect(reverse('cart:list_orders'))


#def client_information(requ):
 #   context = {}
  #  context['all_orders'] = Order.objects.all()

   # return render(request,"listOrders/list_orders.html", context)
