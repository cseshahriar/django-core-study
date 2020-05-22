from django.shortcuts import render

from django.utils import translation
from django.utils.translation import gettext as _

def trans(request):
    # manualy set session lang key
    # from django.utils import translation
    # user_language = 'en'
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY] = user_language 

    # delete session key
    # from django.utils import translation
    # if translation.LANGUAGE_SESSION_KEY in request.session:
    #     del request.session[translation.LANGUAGE_SESSION_KEY] 

    # translate from viw 
    page_title = _('Translation')  

    context = {
        'page_title': page_title 
    }
    return render(request, 'trans/trans.html', context) 
