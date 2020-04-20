from django.db import models
from datetime import timedelta, datetime, date
from django.db.models.signals import pre_save, post_save
from django.utils.encoding import smart_text
from django.utils import timezone
from django.utils.text import slugify
from django.utils.timesince import timesince
from django.urls import reverse

PUBLISH_CHOICES = [
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
]

class Post(models.Model):
    active = models.BooleanField(default=True) #empty in the database
    title = models.CharField(max_length=240, verbose_name='Post title',unique=True, error_messages={
                                "unique": "This title is not unique, please try again.",
                                "blank": "This field is not full, please try again."},
                                help_text='Must be a unique title.')
    slug            = models.SlugField(null=True, blank=True)
    content         = models.TextField(null=True, blank=True)
    publish         = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count      = models.IntegerField(default=0)
    publish_date    = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email    = models.EmailField(max_length=240, null=True, blank=True)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self): #
        return self.title

    def get_absolute_url(self):
        return reverse('post_single', kwargs={'slug': self.slug}) # new

