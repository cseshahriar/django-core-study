from django import forms 
from .models import Student, Mark 


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = [
            'name',
            'gender',
            'age',
        ]

        labels = {
            'name': 'Name',
            'gender': 'Gender',
            'age': 'Age'
        }


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark

        fields = [
            'class_name',
            'english',
            'bangla'
        ]

        widget = {
            'class_name': forms.TextInput(attrs={'class': 'formset-field'}),
            'english': forms.TextInput(attrs={'class': 'formset-field'}),
            'bangla': forms.TextInput(attrs={'class': 'formset-field'}),
        }