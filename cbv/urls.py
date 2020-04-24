from django.urls import path
from django.views.generic.base import TemplateView
from cbv.views import ContactPageView

urlpatterns = [
    path('about/', TemplateView.as_view(template_name='cbv/about.html'), name='about'), # no need views
    path('contact/', ContactPageView.as_view(), name='contact') # no need views
]
