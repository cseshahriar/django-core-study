from django.db.models import Q
from django.shortcuts import render, redirect  
from .forms import UserCreationForm, UserLoginForm
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import login, logout ,get_user_model
from .models import MyUser, Profile, ActivationProfile
User = get_user_model()


def home(request):
    return render(request, 'accounts/home.html', {})



def register(request, *args, **kwargs): 
    form = UserCreationForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        print('User has been created')
        return redirect('/account/login/') 
    
    context = {'form': form}
    return render(request, 'accounts/register.html', context) 


def user_login(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None) 

    if form.is_valid():
        user_obj = form.cleaned_data.get("user_obj")
        login(request, user_obj)  
        return redirect('/account/home/')  

    context = {
        'form': form 
    }
    return render(request, 'accounts/login.html', context) 


def user_logout(request):
    logout(request)
    return redirect('/account/login/')  


def activate_user_view(request, code=None, *args, **kwargs):
    if code: 
        act_profile_qs = ActivationProfile.objects.filter(key=code)
        if act_profile_qs.exists() and act_profile_qs.count() ==1:
            act_obj = act_profile_qs.first()
            if not act_obj.expired:
                user_obj = act_obj.user 
                user_obj.is_active = True  
                user_obj.save()
                act_obj.expired = True  
                act_obj.save() 
                return HttpResponseRedirect("/account/login") 
    # invalid code 
    return HttpResponseRedirect("/account/login") 
