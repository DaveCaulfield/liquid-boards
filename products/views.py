from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """ a View to return allproducts page """

    products = Product.objects.all()

    context = {
        'products': products,
    }
 
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ a View to return individual product details page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
 
    return render(request, 'products/product_detail.html', context)
