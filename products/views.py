from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.


def all_products(request):
    """ a View to return allproducts page """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(brand__icontains=query) 
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }
 
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ a View to return individual product details page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
 
    return render(request, 'products/product_detail.html', context)