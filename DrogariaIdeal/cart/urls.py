from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    url(r'^show_cart/', views.show_cart, name = 'show_cart'),
    url(r'^remove_from_cart/(?P<product_id>[0-9]+)/', views.remove_from_cart, name="remove_from_cart"),
    url(r'^list_orders/', views.list_orders, name='list_orders'),
    url(r'^list_order_history/', views.list_order_history, name='list_order_history'),
    url(r'^list_products_order/(?P<order_id>[0-9]+)/', views.list_products_order, name='list_products_order'),
    url(r'^cancel_order/(?P<order_id>[0-9]+)/', views.cancel_order, name='cancel_order'),
    url(r'^send_order/(?P<order_id>[0-9]+)/', views.send_order, name='send_order'),

]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
