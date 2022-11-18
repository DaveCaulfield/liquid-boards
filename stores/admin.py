from django.contrib import admin
from .models import Store, StoreAddress
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    """
    backend store admin area
    """
    list_display = ('name', 'location',
                    'owner',
                    )

    fields = ('name',
              'location',
              'about',
              'owner',
              'logo_image',
              'logo_url',
              'featured_image',
              'image_url',
              )

    list_filter = ('name', 'location', 'owner')
    search_fields = ['name', 'location', 'owner']



@admin.register(StoreAddress)
class StoreAddressAdmin(admin.ModelAdmin):
    """
    backend store address admin area
    """
    list_display = (
                    'store',
                    'phone_number',
                    'email',
                    'street_address1',
                    'street_address2',
                    'town_or_city',
                    'county',
                    'country',
                    'postcode',  
                    )

    list_filter = ('country', 'store')
    search_fields = ['name', 'email', 'phone_number']