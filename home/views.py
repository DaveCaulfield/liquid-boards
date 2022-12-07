from django.shortcuts import render


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


def privacy(request):
    """
    a View to return the privacy policy page
    """
    return render(request, 'home/privacy_policy.html')