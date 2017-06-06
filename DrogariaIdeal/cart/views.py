# encoding: utf-8
import sys
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from . import cart
from .forms import Create_Order_Form
from .models import Order, ProductOrder
from users.models import CustomUser
import pusher

@login_required
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
            print("-------------------------------------------------------------")
            print(order_form.instance.payment)
            order_form.instance.user = request.user.id
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

            #pusher config
            pusher_client = pusher.Pusher(
                app_id='348802',
                key='a36f6ffa5a7dc96035a0',
                secret='4980033d3fe10039b9ff',
                ssl=True
            )
            
            pusher_client.trigger('my-channel', 'my-event', {'message': 'Voce tem um novo pedido, confira a pagina de pedidos para mais informações'})





            url = reverse('cart:list_products_order', kwargs={"order_id":order_form.instance.id})

            return HttpResponseRedirect(url)

        return render(request, "show_cart/show_cart.html", context)

    else:
        order_form = Create_Order_Form()
        context["form"] = order_form
        return render(request, "show_cart/show_cart.html", context)


@login_required
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


@login_required
def list_orders(request):

    context = {}
    if request.user.is_superuser:
        context['all_orders'] = Order.objects.filter(state = Order.STATE[0][0])
    else:
        context['all_orders'] = Order.objects.filter(user = request.user.id, state = Order.STATE[0][0])

    return render(request,"listOrders/list_orders.html", context)

@login_required
def list_order_history(request):

    context = {}

    context['user'] = request.user
    if request.user.is_superuser:
        context['all_orders'] = Order.objects.filter()
    else:
        context['all_orders'] = Order.objects.filter(user = request.user.id)

    return render(request,"listOrders/list_order_history.html", context)

@login_required
def list_products_order(request,order_id):
    context = {}
    products = []
    amount = []
    main_order = Order.objects.get(id=order_id)
    context["client"] = CustomUser.objects.get(id= main_order.user)
    context["total_price"] = main_order.total_price
    context['product_order'] = main_order.orders.all()
    context['order'] = main_order
    return render(request,"listProductsOrder/list_products_order.html", context)


@login_required
def cancel_order(request, order_id):
    order = Order.objects.get(id = order_id)
    order.state = Order.STATE[2][0]
    order.save()
    return HttpResponseRedirect(reverse('cart:list_orders'))


def send_order(request,order_id):
    order = Order.objects.get(id = order_id)
    order.state = 'delivered'
    order.save()
    return HttpResponseRedirect(reverse('cart:list_orders'))

   
