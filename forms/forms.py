from django import forms
from .models import Post

# django forms
SOME_CHOICES = [
    ('db-value', 'Display Value'),
    ('db-value1', 'Display Value'),
]

INTS_CHOICES = [tuple([x,x]) for x in range(0,10)]
YEARS = [x for x in range(1980, 2050)]

class SearchForm(forms.Form):
    date_field  = forms.DateField(widget=forms.SelectDateWidget)
    date_field2  = forms.DateField(initial="2020-01-01", widget=forms.SelectDateWidget(years=YEARS))
    some_text = forms.CharField(label="Text Level", widget=forms.Textarea(attrs={"rows":4, "cols":10}))
    choices1 = forms.CharField(widget=forms.Select(choices=INTS_CHOICES))
    choices2 = forms.CharField(widget=forms.RadioSelect(choices=SOME_CHOICES))
    choices3 = forms.CharField(widget=forms.SelectMultiple(choices=SOME_CHOICES))
    choices3 = forms.CharField(widget=forms.CheckboxSelectMultiple(choices=SOME_CHOICES))
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=5)
    email = forms.EmailField(max_length=255)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['some_text'].initial= 'Text'
        self.fields['boolean'].initial= True

    # validation
    def clean_integer(self, *args, **kwargs): #clean_field_name
        integer = self.cleaned_data.get("integer") # get field data
        if integer < 10:
            raise forms.ValidationError("The integer must be grater than 10")
        else:
            return integer

    def clean_some_text(self, *args, **kwargs):
        some_text = forms.cleaned_data.get('some_text')
        if len(some_text) < 3:
            raise forms.ValidationError('Ensure the text is greater that 3')
        return some_text


# Model form
class PostModelForm(forms.ModelForm):

    error_css_class = 'error'
    required_css_class = 'required' 

    # custom error message and por practice for model form field, but its ok form form field
    # title = forms.CharField( 
    #     max_length=120, 
    #     label="Title",
    #     help_text="some help text", 
    #     error_messages = {
    #     "required": "The title field is required"
    #     }
    # )

    class Meta():
        model = Post
        fields = ['user', 'title', 'content', 'image']
        exclude = ['slug'] 
        labels = {
            'title': 'This i title' 
        }
        help_text = {
            'title': 'Title must greater than 3 char!'
        }
        error_messages = {
            "title": {
                'max_length': 'This title is too long',
                'required': 'Title is required',
            },
            'slug': {
                'unique': 'Slug must be unique' 
            },
        }

        def __init__(self, *args, **kwargs):
            super(PostModelForm, self).__init__(*args, **kwargs)  
            self.fields["title"].widget = forms.Textarea()   #not working 

    # validation
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        raise forms.ValidationError("Title is required")
        # return title

    # save method customize
    # def save(self, commit=True, *args, **kwargs):
    #     obj = super(PostModelForm, self).save(commit=False, *args, **kwargs)
    #     # if any table required field is not present
    #     obj.publish = True # if not present, required fild
    #     if commit:
    #         obj.save()
    #     return obj


