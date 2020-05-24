from django.urls import path, re_path
from .views import home, register, user_login, user_logout, activate_user_view


urlpatterns = [
    path('home/', home, name='home'), 
    path('register/', register, name='user_register'),   
    path('login/', user_login, name='user_login'),  
    path('logout/', user_logout, name='user_logout'), 
    re_path(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='user_activate'),   
] 
