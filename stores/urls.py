from . import views
from django.urls import path

urlpatterns = [
    path('', views.StoreList.as_view(), name='stores'),
]