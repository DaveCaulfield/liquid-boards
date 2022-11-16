from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Stores(models.Model):
    name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    featured_image = CloudinaryField('image', default='placeholder') 
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False) 
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)    
    county = models.CharField(max_length=80, null=True, blank=True)
    country = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        """
        Magic Method, returns a string description of the object
        """
        return self.title
