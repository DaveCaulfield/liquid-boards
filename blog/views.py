from django.shortcuts import render
from django.views import generic
from .models import Blog


class BlogList(generic.ListView):
    """
    display list of all blog posts
    """
    model = Blog
    queryset = Blog.objects.all().order_by('-created_on')
    template_name = 'blog/blog.html'
    paginate_by = 6



