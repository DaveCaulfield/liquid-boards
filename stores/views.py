from django.shortcuts import render
from django.views import generic, View
from .models import Store


class StoreList(generic.ListView):
    """
    display list of all stores
    """
    model = Store
    queryset = Store.objects.all()
    template_name = 'stores/stores.html'
    paginate_by = 3