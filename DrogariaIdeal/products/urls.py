from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    url(r'^create_product/', views.create_product, name="create_product"),
    url(r'^list_products/', views.list_products, name="list_products"),
    url(r'^delete_products/(?P<product_id>[0-9]+)/', views.delete_products, name="delete_products"),
]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
