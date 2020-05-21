from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True, unique=True)
    image = models.ImageField(upload_to="media", blank=True, null=True)
    content = models.TextField()
    publish = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        auto_now=True, auto_now_add=False)  # auto working
    updated_at = models.DateTimeField(
        auto_now=False, auto_now_add=True)  # auto working 

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

