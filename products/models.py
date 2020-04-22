from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from .validators import validate_author_email
from django.db.models.signals import pre_save, post_save #mode event
from datetime import timedelta, datetime, date
from django.utils.timesince import timesince

# model query set
class ProductModelQuerySet(models.query.QuerySet):
    # return active products
    def active(self):
        return self.filter(active=True)

    # product filter by title
    def product_by_title(self, value):
        return self.filter(title__icontains=value)

# model manager
class ProductModelManager(models.Manager):
    # setup queryset for manager
    def get_queryset(self):
        return ProductModelQuerySet(self.model, using=self._db)

    # return all active product from this model
    def all_active_products(self, *args, **kwargs):
        #qs = super(ProductModelManager, self).all(*args, **kwargs).active() # active method from queryset
        qs = self.get_queryset().active()
        return qs

    def get_timeframe(self, date1, date2):
        qs = self.get_queryset()
        qs_time_1 = qs.filter(publish_date__gte=date1)
        qs_time_2 = qs_time_1.filter(publish_date__gte=date2)
        # final_qs = (qs_time_1 | qs_time_2).distinct()
        return qs_time_2


PUBLISH_CHOICE = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
)

class Product(models.Model):
    title   = models.CharField(
                max_length=255,
                verbose_name='Product Title',
                unique=True,
                error_messages={
                    "unique": "This title is not unique, please try again",
                },
                help_text="Must be a unique title")
    slug    = models.SlugField(null=True, blank=True)
    content = models.TextField(null=True, blank=True) # blank=True means required
    publish = models.CharField(max_length=120, choices=PUBLISH_CHOICE, default='draft')
    active  = models.BooleanField(default=True) # null=True
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email = models.CharField(max_length=255, null=True, blank=True, validators=[validate_author_email])
    created_at = models.DateTimeField(auto_now=True) # when product created
    updated_at = models.DateTimeField(auto_now_add=True) # when last changed

    objects = ProductModelManager() # initialize

    def save(self, *args, **kwargs):
        '''
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        qs_exists = Product.objects.filter(slug=self.slug).exists()
        if qs_exists:
            self.slug = self.slug + '-' +get_random_string(length=12)
            '''
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def age(self):
        if self.publish == 'publish':
            now = datetime.now()
            publish_time = datetime.combine(self.publish_date, datetime.now().min.time())
            try:
                difference = now - publish_time
            except:
                return 'Unknown'
            if difference <= timedelta(minutes=1):
                return 'just now'
            return '{time} ago'.format(time=timesince(publish_time).split(', ')[0])

    class Meta():
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        # unique_together = [('title', 'slug')]


# before save
def product_pre_save_recerver(sender, instance, *args, **kwargs):
    print('Before save')
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)
        instance.save()

pre_save.connect(product_pre_save_recerver, sender=Product)


# After save
def product_post_save_recerver(sender, instance, created, *args, **kwargs):
    print('After save')
    if created:
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()

post_save.connect(product_post_save_recerver, sender=Product)




