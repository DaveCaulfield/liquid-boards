from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    brand = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Review model. Authenticated members can review a product
    """

    user = models.ForeignKey(UserProfile, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    body = models.TextField(max_length=500, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        """
        Orders reviews by date created - newest first
        """
        ordering = ['-created_on']

    def __str__(self):
        """Magic Method, returns a string description of the object"""
        return f"Review {self.body} by {self.user}" 

