from django.shortcuts import render, Http404, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PostModelForm
from django.db.models import Q
from .models import Post

'''
# login require
# @login_required(login_url='/login')
def post_list_view(request):
    qs = Post.objects.all()
    context = {
        'posts': qs
    }
    if request.user.is_authenticated:
        template = 'posts/list.html'
    else:
        # template = 'posts/public-list.html'
        # raise Http404 # if not authenticate
        return redirect('login') #url name
    return render(request, template, context)
'''

# list view
def post_list_view(request):
    query = request.GET.get('q', None) # None is default
    qs = Post.objects.all()
    # search
    if query is not None:
        #qs = qs.filter(title__icontains=query) # single field lookup
        qs = qs.filter(Q(title__icontains=query) | Q(content__icontains=query))
    context = {'posts': qs }
    template = 'posts/list.html'
    return render(request, template, context)

# detail view
def single_post(request, slug=None):
    qs = get_object_or_404(Post, slug=slug)
    context = {'post': qs }
    template = 'posts/single.html'
    return render(request, template, context)

# @login_required
def post_create_view(request):
    form = PostModelForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, 'Created a new blog post!')
            # context = {'form': PostModelForm()}  # post create after redirect post create form
            return redirect('post_list')

    template = 'posts/create.html'
    return render(request, template, context)

#@login_required
def post_update_view(request, id=None):
    obj = get_object_or_404(Post, id=id)
    form = PostModelForm(request.POST or None, instance=obj)
    context = {'form': form}

    if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, 'Updated post!')
            # context = {'form': PostModelForm()}  # post create after redirect post create form
            return redirect('post_list')

    template = 'posts/edit.html'
    return render(request, template, context)

# delete view
def delete_post(request, id=None):
    instance = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        instance.delete()
        messages.success(request, 'Post Deleted!')
        return redirect('post_list')

    context = {'instance': instance }
    template = 'posts/delete.html'
    return render(request, template, context)
