from django.urls import path
from .views import list, create

urlpatterns = [
    path('formset/student/create', create, name='formset_create'),
    path('formset/student/list', list, name='formset_list'), 
]
