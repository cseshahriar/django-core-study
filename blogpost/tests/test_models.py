from django.test import TestCase
from blogpost.models import Post
from django.utils.text import slugify

class PostModelTestCase(TestCase):
    def setUp(self):
        '''
        test database
        '''
        Post.objects.create(title='New Title', slug='new-title')

    # post creating method
    def create_post(self, title='This is a title'):
        Post.objects.create(title=title)

    def test_post_title(self):
        '''
        test case
        '''
        obj = Post.objects.get(slug='new-title') # get object by slug test
        self.assertEqual(obj.title, 'New Title')
        self.assertTrue(obj.content == "") # maybe i want to chagne

    def test_post_slug(self):
        # generate slug and testing
        title1 = 'another title abc'
        title2 = 'another title abc2'
        title3 = 'another title abc3'
        slug1 = slugify(title1)
        slug2 = slugify(title2)
        slug3 = slugify(title3)
        obj1 = self.create_post(title=title1) # creating item 1
        obj2 = self.create_post(title=title2) # creating item 2
        obj3 = self.create_post(title=title3) # creating item 3

        # self.assertEqual(obj1.slug, slug1)
        #self.assertEqual(obj2.slug, slug2) # new
        #self.assertNotEqual(obj3.slug, slug3) # update for unique

    def test_post_qs(self):
        title1 = 'another title abc'
        obj1 = self.create_post(title=title1) # creating item 1
        obj2 = self.create_post(title=title1) # creating item 2
        obj3 = self.create_post(title=title1) # creating item 3
        qs = Post.objects.filter(title=title1)
        #self.assertEqual(qs.count(), 3)
        # object 2 is created or not
        #qs2 = Post.objects.filter(slug=obj1.slug)
        #self.assertEqual(qs2.count(), 1)
