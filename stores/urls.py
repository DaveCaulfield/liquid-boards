from . import views
from django.urls import path

urlpatterns = [
    path('', views.StoreList.as_view(), name='stores'),
    path('<int:store_id>/', views.store_detail, name='store_detail'),
]