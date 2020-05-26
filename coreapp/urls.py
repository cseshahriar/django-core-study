from django.contrib import admin
from django.urls import path, include
from django.conf import settings 

from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


# without translation 
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('form/', include('forms.urls')),
    path('account/', include('accounts.urls')), 
    path('template/', include('temp.urls')),   
    path('', include('category.urls')),   
] 

urlpatterns += i18n_patterns(
    path('', include('translation.urls')),    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
