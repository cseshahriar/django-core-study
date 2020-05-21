from django.urls import path
from .views import search, modelFormView

urlpatterns = [
    path('', search, name='search-form'),
    path('model', modelFormView, name='model-form'), 
]
