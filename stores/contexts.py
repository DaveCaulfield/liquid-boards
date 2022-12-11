from .models import Store


def stores(request):
    return {
        'stores': Store.objects.all()
    }
