from django.urls import path 
from .views import temp, create

urlpatterns = [
    path('temp/', temp, name='temp')  ,
    path('create/', create, name="temp-create") ,
]
