from django.contrib import admin

from .models import BlogPost, Comment, Rating, Following

from easylearn.users.models import User

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['writer', 'text']
    extra = 1
    max_num = 10

class RatingInline(admin.TabularInline):
    '''Tabular Inline View for Rating'''

    model = Rating
    max_num = 10
    extra = 1
    fields = ['rater', 'value']
    readonly_fields=['rate_date']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'writer']
    inlines = [CommentInline, RatingInline]
    list_display = ['title', 'writer', 'get_summary']
    list_filter = ['create_date']


@admin.register(Following)
class FollowingAdmin(admin.ModelAdmin):
    '''Admin View for Following'''
    pass
