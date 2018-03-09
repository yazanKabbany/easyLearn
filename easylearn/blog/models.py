from django.db import models

from slugify import UniqueSlugify



def check_unique_slug(text, *args):
    return not BlogPost.objects.filter(slug=text).exists()

# Create your models here.
class BlogPost(models.Model):
    """Model definition for BlogPost."""

    # TODO: Define fields here
    title = models.CharField(max_length=50, blank = False)
    slug = models.SlugField(blank=True)
    text = models.TextField(blank=False)
    writer = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for BlogPost."""

        verbose_name = 'Blog post'
        verbose_name_plural = 'Blog posts'

    def __str__(self):
        """Unicode representation of BlogPost."""
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            unique_slugify = UniqueSlugify(unique_check=check_unique_slug)
            self.slug = unique_slugify(self.title)
        return super().save(*args, **kwargs)