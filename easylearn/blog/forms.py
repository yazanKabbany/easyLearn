from django import forms

from blog.models import BlogPost

class BlogPostForm(forms.ModelForm):
    """BlogPostForm definition."""
    text = forms.CharField(widget=forms.Textarea(attrs={'cols':100}), 
    max_length=4000, required=True)

    class Meta:

        model = BlogPost
        fields = ('title', 'text',)