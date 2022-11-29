from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """
    a View to return the bag page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of a specific item to the bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})  # http session variable

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.brand} {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'{product.brand} {product.name} added to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust a quantity of a specific item to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})  # http session variable

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.brand} {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'{product.brand} {product.name} removed from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove item from bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})  # http session variable

        bag.pop(item_id)
        messages.success(request, f'{product.brand} {product.name} removed from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
