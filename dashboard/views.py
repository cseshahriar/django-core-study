from blog.models import Post
from django.shortcuts import render
from products.models import Product

from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView, TemplateResponseMixin, ContextMixin

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# login require mixin
class LoginRequiredMixin(object):
    # @classmethod
    # def as_view(cls, **kwargs):
    #     view = super(LoginRequiredMixin, cls).as_view(**kwargs)
    #     return login_required(view)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MyView, self).dispatch(request, *args, **kwargs)

# Base View and mixin
class MyView(LoginRequiredMixin, ContextMixin, TemplateResponseMixin, View):

    template_name = 'someview.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(MyView, self).dispatch(request, *args, **kwargs)


# Template view
class DashboardTemplateView(TemplateView):

    template_name = "dashboard.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        products = Product.objects.all()
        posts = Post.objects.all()
        context = {
            'products': products,
            'posts': posts,
        }
        return context
