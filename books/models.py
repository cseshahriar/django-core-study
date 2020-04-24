import random
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils.crypto import get_random_string

class Book(models.Model):
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='book_add', on_delete=models.CASCADE)
    last_edited_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='book_edit', on_delete=models.CASCADE)
    title       = models.CharField(max_length=120)
    slug        = models.SlugField(null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at  = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta():
        ordering = ["-created_at", "-updated_at"]
        unique_together = ['title', 'slug']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        # for unique slug
        qs_exists = Book.objects.filter(slug=self.slug).exists()
        if qs_exists:
            self.slug = self.slug + '-' +get_random_string(length=12)
        super(Book, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'slug':self.slug})


