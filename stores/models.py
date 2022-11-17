from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Store(models.Model):
    """
    Model for a Store
    """
    name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200,null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
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
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name="store")
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)    
    county = models.CharField(max_length=80, null=True, blank=True)
    country = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False) 

    def __str__(self):
        """
        Magic Method, returns a string description of the object
        """
        return self.town_or_city