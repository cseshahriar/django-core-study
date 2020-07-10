from django.test import TestCase
from blogpost.models import Post
from django.utils.text import slugify
from blogpost.forms import PostForm
from django.utils import timezone

class PostFormTestCase(TestCase):
    def test_valid_form(self):
        title = 'A new title'
        slug = 'a-new-title'
        content = "some content here"
        obj = Post.objects.create(title=title, slug=slug, publish=timezone.now())
        data = {'title':obj.title, 'slug': obj.slug, 'publish': obj.publish, 'content': content}
        form = PostForm(data=data) # PostForm(request.POST)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get('title'), obj.title)
        self.assertNotEqual(form.cleaned_data.get('content'), "A new title")

    def test_invalid_form(self):
        title = 'A new title'
        slug = 'a-new-title'
        content = "some content here"
        obj = Post.objects.create(title=title, slug=slug, publish=timezone.now(), content=content)
        data = {'title':obj.title, 'slug': obj.slug, 'publish': obj.publish, 'content': ''}
        form = PostForm(data=data) # PostForm(request.POST)
        self.assertFalse(form.is_valid())
        print(form.errors)
        self.assertTrue(form.errors)
