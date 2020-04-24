from django.urls import path
from .views import BookListView, BookDetail, BookCreate, BookUpdate, BookDelete

urlpatterns = [
    path('list/', BookListView.as_view(), name='book-list'),
    path('create/', BookCreate.as_view(), name='book-create'),
    path('<slug:slug>/', BookDetail.as_view(), name='book-detail'),
    path('<slug:slug>/update/', BookUpdate.as_view(), name='book-update'),
    path('<slug:slug>/delete/', BookDelete.as_view(), name='book-delete'),
]
