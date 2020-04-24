from django import forms
from .models import Book
from django.utils.text import slugify

class BookForm(forms.ModelForm):
    class Meta():
        model = Book
        fields = ['title', 'description']
        # fields = "__all__"

    # def clean_title(self):
    #     title = self.clean_data['title']
    #     slug = slugify(title)
    #     try:
    #         book = Book.objects.get(slug=slug)
    #         raise forms.ValidationError("Title already exists. Please try a diffent one.")
    #     except Book.DoesNotExist:
    #         return title
    #     except:
    #         raise forms.ValidationError("Title already exists. Please try a diffent one.")

