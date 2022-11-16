from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify




class Blog(models.Model):
    """
    Model for Blog postings
    """
    title = models.CharField(
        max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog")
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField(blank=True, null=True)
    excerpt = models.TextField(blank=True)
    likes = models.ManyToManyField(
        User, related_name='like_blog', blank=True)
    
    class Meta:
        """
        Orders blog postings by date created - newest first
        """
        ordering = ['-created_on']


    def __str__(self):
        """
        Magic Method, returns a string description of the object
        """
        return self.title

    def number_of_likes(self):
        """
        Helper method, returns the amount of likes on a blog post
        """
        return self.likes.count()

    def save(self, *args, **kwargs):
        """
        slugify function from learndjango.com
        """
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Comments model. Authenticated members can comment on a blog
    """
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name="comments")
    commenter = models.ForeignKey(UserProfile, related_name='comments', on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:  
        """
        Orders blog posts by date created - oldest first
        """
        ordering = ['created_on']

    def __str__(self):
        """Magic Method, returns a string description of the object"""
        return f"Comment {self.body} by {self.name}"