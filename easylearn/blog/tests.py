from django.test import TestCase

from .models import BlogPost
from easylearn.users.models import User

# Create your tests here.

class BlogPostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('yazan')
        self.user2 = User.objects.create_user('habib')        
    def test_unique_slug(self):
        """
        two post with identical titles should different slugs
        """
        repeated_title = "good blog"
        post = BlogPost()
        post.title = repeated_title
        post.writer = self.user
        post.text = "some radom text"
        post.save()

        post2 = BlogPost()
        post2.title = repeated_title
        post2.writer = self.user2
        post2.text = "another random text"
        post2.save()

        self.assertNotEqual(post.slug, post2.slug)
    
    def test_has_slug(self):
        """
        post slug is not an empty string
        """
        post = BlogPost.objects.create(title='some title', 
                                        text='some text', writer=self.user)
        self.assertNotEqual(post.slug, '')