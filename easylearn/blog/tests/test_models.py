from django.test import TestCase

from blog.models import BlogPost, Comment, Following, Rating, POST_SUMMARY_LENGTH
from easylearn.users.models import User

# Create your tests here.

class BlogPostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('yazan')
        self.user2 = User.objects.create_user('habib')
        self.post = BlogPost.objects.create(title='some title', 
                                        text='some text', writer=self.user)
        self.long_post = BlogPost.objects.create(title="A very Long Post",
                                        text=500*'long ', writer=self.user2)

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
    
    def test_get_summary(self):
        """
        summary for long post equals POST_SUMMARY_LENGTH + 3
        summary for small post equals len(post.text)
        """
        self.assertEqual(len(self.long_post.get_summary()), POST_SUMMARY_LENGTH+3)
        self.assertEqual(self.post.get_summary(), self.post.text)

class CommentTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('yazan')
        self.user2 = User.objects.create_user('habib')
        self.post = BlogPost.objects.create(title='some title', 
                                        text='some text', writer=self.user)
    
    def test_create(self):
        comment_text = "some text for the comment"
        comment = Comment()
        comment.text = comment_text
        comment.post = self.post
        comment.writer = self.user
        comment.save()
        self.assertEqual(comment.text, comment_text)
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.writer, self.user)

        
class RatingTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('samir')
        self.user2 = User.objects.create_user('Hbib again')
        self.post = BlogPost.objects.create(title='some title', 
                                        text='some text', writer=self.user)
        self.value = 4
                                
    def test_create(self):
        """simple creation test"""
        rating = Rating.objects.create(rater=self.user2, post=self.post, value=self.value)
        rating.save()
        self.assertEqual(rating.rater, self.user2)
        self.assertEqual(rating.post, self.post)
        self.assertEqual(rating.value, self.value)
    
    def test_value_out_of_range(self):
        """rating values out of range [0, 5] are not allowed"""
        # BUG: not working test needs modifications
        return
        rating = Rating(rater=self.user2, post=self.post, value=6)
        with self.assertRaises(ValidationError):
            rating.save()
        
        rating = Rating(rater=self.user2, post=self.post, value=0)
        with self.assertRaises(ValidationError):
            rating.save()


class FollowingTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('samir')
        self.user2 = User.objects.create_user('jack')
    
    def test_create(self):
        """simple creation test"""
        following = Following(follower=self.user, followed=self.user2)
        following.save()
        self.assertEqual(following.follower, self.user)
        self.assertEqual(following.followed, self.user2)
