from django.urls import path
from . import views 



urlpatterns = [
    path("news", views.new_product),
    path("", views.productss), 
    
    
]