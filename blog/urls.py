from django.urls import path
from .views import post_list_view, single_post, post_create_view, post_update_view, delete_post

urlpatterns = [
    path('list/', post_list_view, name='post_list'),
    path('create/form', post_create_view, name='post_create'),
    path('<slug:slug>', single_post, name='post_single'),
    path('edit/<int:id>', post_update_view, name='post_edit'),
    path('delete/<int:id>', delete_post, name='post_delete'),
]
