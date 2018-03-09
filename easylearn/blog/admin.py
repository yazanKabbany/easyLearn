from django.contrib import admin

from .models import BlogPost, Comment

from easylearn.users.models import User

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['writer', 'text']
    extra = 1
    max_num = 10

class BlogPostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['title', 'writer', 'get_summary']


admin.site.register(BlogPost, BlogPostAdmin)
