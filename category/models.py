from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from django.db.models.signals import pre_save  # Signals
# import the unique_slug_generator from .utils.py
from .utils import unique_slug_generator 


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)  
    slug = models.SlugField(null=True, blank=True, max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name
    
    class MPTTMeta:
        order_insertion_by = ['name']


def category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(category_pre_save_receiver, sender=Category) 

