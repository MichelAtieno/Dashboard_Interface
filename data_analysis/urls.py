from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard', index, name="index"),
    path('staff/', staff, name="staff"),
    path('staff/detail/<int:pk>/', staff_detail, name="staff-detail"),
    path('product/', product, name="product"),
    path('product/delete/<int:pk>/', product_delete, name="product-delete"),
    path('product/update/<int:pk>/', product_update, name="product-update"),
    path('order/', order, name="order"),
    
  
] 