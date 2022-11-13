from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'),
    
    ]