from django.urls import path, re_path  
from .views import category_view

urlpatterns = [
    path('categories/', category_view), 
]

