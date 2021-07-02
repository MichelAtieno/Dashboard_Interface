from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard', index, name="index"),
    path('staff/', staff, name="staff"),
    path('product/', product, name="product"),
    path('product/delete/<int:pk>/', product_delete, name="product-delete"),
    path('order/', order, name="order"),
    
  
] 