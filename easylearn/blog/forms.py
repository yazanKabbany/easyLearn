from django import forms

from blog.models import BlogPost

class BlogPostForm(forms.ModelForm):
    """BlogPostForm definition."""
    text = forms.CharField(widget=forms.Textarea(attrs={'cols':100, 'class':'arabic-text', 
    'id':'post-text'}), 
    max_length=4000, required=True, label='المنشور')
    title = forms.CharField(widget = forms.TextInput(attrs={'cols':50, 'class':'arabic-text'}),
     max_length=50, required=True, label='العنوان')

    class Meta:

        model = BlogPost
        fields = ('title', 'text',)