from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import Http404

from django.contrib import messages

from django.core.paginator import Paginator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin, ModelFormMixin

from .models import Book
from .forms import BookForm


class MultipleObjectMixin(object):
      def get_object(self, queryset=None, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            try:
                obj = self.model.objects.get(slug=slug)
            except self.model.MultipleObjectsReturned:
                obj = self.get_queryset().first()
            except:
                raise Http404
            return obj
        raise Http404


# Class base list view
class BookListView(ListView):
    model = Book
    paginate_by = 5  # if pagination is desired

    # template_name = 'books/user_list.html'  # Default: <app_label>/<model_name>_list.html
    # context_object_name = 'books'  # Default: object_list
    # queryset = Book.objects.all()  # Default: Model.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = super(BookListView, self).get_queryset(*args, **kwargs).order_by("-created_at")
        return qs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


# Class base details view
class BookDetail(ModelFormMixin, MultipleObjectMixin, DetailView):
    model = Book

    # ModelFormMinix
    form_class = BookForm # it's a form view, not detail view

    # def get_object(self, queryset=None, *args, **kwargs):
    #     slug = self.kwargs.get('slug')
    #     if slug:
    #         try:
    #             obj = self.model.objects.get(slug=slug)
    #         except self.model.MultipleObjectsReturned:
    #             obj = self.get_queryset().first()
    #         except:
    #             return None
    #         return obj
    #     return None

    # template_name = books/book_detail.html # app name/singular_app_name_detail.html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    # update form data
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            self.object = self.get_object()
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, 'Book updated!')
        return reverse('book-list')


# Class base create view
class BookCreate(CreateView):
    # model = Book
    # fields = ['title', 'description']
    form_class = BookForm
    template_name = 'books/book_form.html'

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        # form.instance.last_edited_by = self.request.user
        return super(BookCreate, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Book created!')
        return reverse('book-list')

# Class base update view
class BookUpdate(MultipleObjectMixin, UpdateView):
    model = Book
    # fields = ['title', 'description']
    form_class = BookForm
    template_name = 'books/book_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Book updated!')
        return reverse_lazy('book-list')


# Class base delete view
class BookDelete(DeleteView):
    model = Book
    #success_url = reverse_lazy('book-list')
    def get_success_url(self):
        messages.success(self.request, 'Book deleted!')
        return reverse_lazy('book-list')

# Class base form view(for template view or View)
