from django.shortcuts import render, redirect 
from django.forms import modelformset_factory 
from django.db import transaction, IntegrityError
from .forms import StudentForm, MarkForm 
from .models import Student, Mark


def create(request):
    context = {}
    # make formset for MarkForm
    MarksFormset = modelformset_factory(Mark, form=MarkForm,)
    
    # Student form and MarksFormset  
    form = StudentForm(request.POST or None)
    formset = MarksFormset(request.POST or None, queryset=Mark.objects.none(), prefix='marks',)

    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    student = form.save(commit=False) # not save now 
                    student.save() # save 

                    for mark in formset:
                        data = mark.save(commit=False)
                        data.student = student # assign foreignkey obj 
                        data.save()
            except IntegrityError:
                print('Error Encountered')

            return redirect('formset_list')

    # if get request 
    context['formset'] = formset
    context['form'] = form
    return render(request, 'multi_forms/create.html', context)


def list(request):
    datas = Student.objects.all()
    return render(request, 'multi_forms/list.html', {'datas': datas}) 

