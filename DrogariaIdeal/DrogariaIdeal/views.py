from django.shortcuts import render


from products.models import Product


def index(request):
    context = {
        'featured_products': Product.objects.filter(featured=True)
    }
    return render(request, "index.html", context)


def about(request):
    return render(request,"about.html")
