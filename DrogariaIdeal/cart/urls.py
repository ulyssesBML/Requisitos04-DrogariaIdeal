from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    url(r'^show_cart/', views.show_cart, name = 'show_cart'),
    url(r'^remove_from_cart/(?P<product_id>[0-9]+)/', views.remove_from_cart, name="remove_from_cart"),
]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
