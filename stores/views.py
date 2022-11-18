from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from .models import Store, StoreAddress, Staff, StaffAddress


class StoreList(generic.ListView):
    """
    display list of all stores
    """
    model = Store
    queryset = Store.objects.all()
    template_name = 'stores/stores.html'
    paginate_by = 3


def store_detail(request, store_id):
    """ a View to return individual store detail page """

    queryset = Store.objects
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

    