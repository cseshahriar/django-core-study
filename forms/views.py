from django.shortcuts import render
from .forms import SearchForm, PostModelForm

# Create your views here.
def search(request):
    form = SearchForm(request.POST or None) # get request nor error

    # validation
    if form.is_valid():
        print(form.cleaned_data)

    template_name = 'forms/testform.html'
    context = {'form': form}
    return render(request, template_name, context)


def modelFormView(request):
    form = PostModelForm(request.POST or None) 
    if form.is_valid():
        obj = form.save(commit=False) # commit false = get data from form but don't save database 
        obj.title = "title"
        obj.content = "Content"
        obj.save() # commit = true default,  save to database 

    # form error in console 
    if form.has_error:
        # print(form.errors.as_json())
        print(form.errors.as_text())
    # non field errors 
    print(form.non_field_errors)  
    

    template_name = 'forms/model_form.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)
