from django.db import models
from markdown import markdown
from slugify import UniqueSlugify

POST_SUMMARY_LENGTH = 250

def check_unique_slug(text, *args):
    return not BlogPost.objects.filter(slug=text).exists()

# Create your models here.
class BlogPost(models.Model):
    """Model definition for BlogPost."""

    # TODO: Define fields here
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
        # TODO: Implement absolute url
        pass

    def get_summary(self):
        summary = self.text[:POST_SUMMARY_LENGTH]
        if len(self.text) > POST_SUMMARY_LENGTH:
            summary += '...'
        return summary
    
    def get_summary_as_markdown(self):
        return markdown(self.text)


class Comment(models.Model):
    """Model definition for Comment."""

    # TODO: Define fields here
    post = models.ForeignKey(BlogPost, models.CASCADE, blank=False)
    text = models.CharField(max_length=500, blank=False)
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

    def get_absolute_url(self):
        # TODO: implement absolute url
        pass
