from django.urls import path
from dashboard.views import DashboardTemplateView, MyView # Class base view

urlpatterns = [
    path('dashboard/', DashboardTemplateView.as_view(), name='dashboard'),
    path('someview/', MyView.as_view(), name='someview'),
]
