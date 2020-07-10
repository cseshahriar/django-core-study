from django import forms
from django.forms import ModelForm
from django.croe.exceptions import ValidatonError
from django.core.validators

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

# model form
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']
        # exclude = ['title']
        widget = {
            'name': Textarea(attrs={
                'class' : 'form-control',
                'style' : 'text-align:center;',
                'cols':80,
                'rows': 5
            }),
        }
        labels = {
            'name': _('Write your name here'),
            'title': _('Select title please'),
        }
        help_texts = {
            'name': _('Some useful help text'),
        }
        error_messages = {
            'name': {
                'max_lenght': _('this writer\'s name is to long.'),
            }
        }


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']


# save method
# commit = false means it will return an object that han't yet been save to the database
# This is usefll if you want to do custom processing on the object before saving
# Commit is True is default

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    title = forms.CharField(max_length=4, widget=forms.Select(choices=TITLE_CHOICES),)
    birth_date = forms.DateField(required=False)


class BookForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
