from django.contrib import admin
from .models import Stores
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Stores)
class StoresAdmin(admin.ModelAdmin):
    """
    backend administration comment area
    """
    list_display = ('name', 'location',
                    'email', 'phone_number',
                    )

    fields = ('name',
              'location',
              'email', 
              'phone_number',
              'street_address1',
              'street_address2',
              'town_or_city',
              'county',
              'country',
              'postcode',
              )

    list_filter = ('name', 'location')
    search_fields = ['name', 'location']