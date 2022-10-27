from django.shortcuts import render
from django.contrib import messages



# Create your views here.

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LxXsPCrog7RoM46jl2VuOZD3DgPF7MLHQHaeq8qVt02U36FxmBP0YJwCOVHpceVMag3Uuvwm3QZfcmZZnHWFUej00SHyqb1mw',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)