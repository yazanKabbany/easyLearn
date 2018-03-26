from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from markdown import markdown
from slugify import UniqueSlugify

POST_SUMMARY_LENGTH = 250

def check_unique_slug(text, *args):
    return not BlogPost.objects.filter(slug=text).exists()

# Create your models here.
class BlogPost(models.Model):
    """Model definition for BlogPost."""

    title = models.CharField(max_length=50, blank = False)
    slug = models.SlugField(blank=True)
    text = models.TextField(blank=False, max_length=4000)
    writer = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for BlogPost."""

        verbose_name = 'Blog post'
        verbose_name_plural = 'Blog posts'
        ordering = ['-create_date']

    def __str__(self):
        """Unicode representation of BlogPost."""
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            unique_slugify = UniqueSlugify(unique_check=check_unique_slug)
            self.slug = unique_slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:blog_post_slug', kwargs={'slug': self.slug})

    def get_summary(self):
        summary = self.text[:POST_SUMMARY_LENGTH]
        if len(self.text) > POST_SUMMARY_LENGTH:
            summary += '...'
        return summary
    
    def get_summary_as_markdown(self):
        return markdown(self.text)

    def get_rating_avg(self):
        return self.objects.Ratings.aggregate(models.Avg('value'))


class Comment(models.Model):
    """Model definition for Comment."""

    post = models.ForeignKey(BlogPost, models.CASCADE, blank=False)
    text = models.TextField(max_length=500, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=False)

    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-create_date']

    def __str__(self):
        """Unicode representation of Comment."""
        return self.text



class Rating(models.Model):
    """Model definition for Rating."""

    rate_date = models.DateTimeField(auto_now_add=True)
    rater = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='Ratings')
    value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        blank=False
    )

    class Meta:
        """Meta definition for Rating."""

        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        unique_together = ("rater", "post")

    def __str__(self):
        """Unicode representation of Rating."""
        return '{} rates {} with {} start'.format(self.rater, self.post, self.value)


class Following(models.Model):
    """Model definition for Following."""

    follower = models.ForeignKey('users.User', on_delete=models.CASCADE, 
    related_name='followed')
    followed = models.ForeignKey('users.User', on_delete=models.CASCADE,
    related_name='followers')

    class Meta:
        """Meta definition for Following."""

        verbose_name = 'Following'
        verbose_name_plural = 'Followings'
        unique_together = ("follower", "followed")

    def __str__(self):
        """Unicode representation of Following."""
        return '{} follows {}'.format(self.follower, self.followed)
    

