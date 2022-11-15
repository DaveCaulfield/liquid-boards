from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('like/<slug:slug>/', views.BlogLike.as_view(), name='blog_like'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<comment_id>/', views.delete_comment, name='delete_comment'),
    
    ]