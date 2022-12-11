from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Store, StoreAddress


class StoreList(generic.ListView):
    """
    display list of all stores
    """
    model = Store
    queryset = Store.objects.all().order_by('name')
    template_name = 'stores/stores.html'
    paginate_by = 3


def store_detail(request, store_id):
    """
    View to return individual store detail page
    """
    # queryset = Store.objects
    store = get_object_or_404(Store, pk=store_id)
    address = get_object_or_404(StoreAddress, pk=store)
    staff = store.staff.all()

    template = 'stores/store_detail.html'

    context = {
        'store': store,
        'address': address,
        'staff': staff,
    }

    return render(request, template, context)
