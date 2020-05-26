from django.shortcuts import render
from .models import Category

def category_view(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, "categories/list.html", context)
