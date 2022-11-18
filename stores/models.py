from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Store(models.Model):
    """
    Model for a Store
    """
    name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200, null=False, blank=False)
    about = models.TextField(max_length=500, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    logo_url = models.URLField(max_length=1024, null=True, blank=True)
    logo_image = CloudinaryField('logo', default='logo_placeholder')
    owner = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        """
        Magic Method, returns a string description of the object
        """
        return self.name


class StoreAddress(models.Model):
    """
    Model for a Store address
    """
    store = models.OneToOneField(
        Store, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)    
    county = models.CharField(max_length=80, null=True, blank=True)
    country = models.CharField(max_length=80, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        """
        Magic Method, returns a string description of the object
        """
        return f"{self.town_or_city} address"


class Staff(models.Model):
    """
    Model for a Staff members
    """
    first_name = models.CharField(max_length=200, null=False, blank=False)
    surname = models.CharField(max_length=200, null=False, blank=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='staff')
    staff_photo = CloudinaryField('staff', default='staff_placeholder')
    job_title = models.CharField(max_length=200, null=False, blank=False)
    bio = models.TextField(blank=True)
    start_date = models.DateField(null=False, blank=False)
    staff_number = models.CharField(max_length=6, unique=True, null=False, blank=False)

    def __str__(self):
        """
        Magic Method, returns a string description of the object
        """
        return f"Staff member - {self.first_name} {self.surname}"


