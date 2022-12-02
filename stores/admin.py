from django.contrib import admin
from .models import Store, StoreAddress, Staff, StaffAddress
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
              'store_image',
              'store_image_url',
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


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    """
    backend staff admin area
    """
    list_display = (
                    'staff_number',
                    'store',
                    'first_name',
                    'surname',
                    'job_title',
                    'start_date',
                    'staff_number',
                    )

    list_filter = ('surname', 'store', 'staff_number')
    search_fields = ['surname', 'email', 'phone_number', 'staff_number']


@admin.register(StaffAddress)
class StaffAddressAdmin(admin.ModelAdmin):
    """
    backend staff adddress admin area
    """
    list_display = (
                    'staff',
                    'phone_number',
                    'email',
                    'street_address1',
                    'street_address2',
                    'town_or_city',
                    'postcode',
                    )

    list_filter = ('phone_number', 'email')
    search_fields = ['email', 'phone_number']
