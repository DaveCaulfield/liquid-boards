from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import Store


def stores(request):
    return {
        'stores': Store.objects.all()
    }
