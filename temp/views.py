from django.shortcuts import render
from .models import Post 
from .forms import PostCreateForm 


def temp(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'temp/temp.html', context)

def create(request):
    form = PostCreateForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        obj = form.save(commit=True)
        obj.save()
        context = {
            'form': PostCreateForm, 
        }
    return render(request, 'temp/create.html', context) 
