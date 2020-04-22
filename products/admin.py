from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = [
        'title', 'slug', 'content', 'publish',
        'active', 'view_count', 'publish_date',
        'author_email', 'created_at', 'updated_at', 'get_age'
    ]
    readonly_fields = ['created_at', 'updated_at', 'get_age']

    def get_age(self, obj, *args, **kwargs):
        return str(obj.age())

    class Meta():
        model = Product

admin.site.register(Product, ProductAdmin);
