from django.shortcuts import render

# Create your views here.

def index(request):
    """
    a View to return the index page
    """
    
    return render(request, 'home/index.html')


def about(request):
    """
    a View to return the about page
    """
    return render(request, 'home/about.html')
