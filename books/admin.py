from django.contrib import admin
from .models import Book
from .forms import BookForm

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    readonly_fields = ['created_at', 'updated_at', 'added_by', 'last_edited_by']
    form = BookForm

admin.site.register(Book, BookAdmin)

