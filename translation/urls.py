from django.urls import path 
from .views import trans 

urlpatterns = [
    path('trans/', trans, name='trans')  
] 


