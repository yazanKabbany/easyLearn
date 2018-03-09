from django.test import TestCase

from blog.models import BlogPost
from easylearn.users.models import User

# Create your tests here.

class BlogPostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('yazan')
        self.user2 = User.objects.create_user('habib')
        self.post = BlogPost.objects.create(title='some title', 
                                        text='some text', writer=self.user)  
    def test_unique_slug(self):
        """
        two post with identical titles should different slugs
        """
        repeated_title = self.post.title
        
        post2 = BlogPost()
        post2.title = repeated_title
        post2.writer = self.user2
        post2.text = "another random text"
        post2.save()

        self.assertNotEqual(self.post.slug, post2.slug)
    
    def test_has_slug(self):
        """
        post slug is not an empty string
        """
        self.assertNotEqual(self.post.slug, '')
    
    def test_slug_dont_change(self):
        """
        post slug is not changed
        """
        previus_slug = self.post.slug
        self.post.title = "Changed title"
        self.post.save()
        self.assertEqual(previus_slug, self.post.slug)
        