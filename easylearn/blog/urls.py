from django.urls import include, path
from blog.views import BlogPostCreateView, BlogPostDetailView, BlogPostFeedListView, RecommendedBlogPostsListView, rate_view, comment_view, preview_view
app_name = 'blog'

urlpatterns = [
    path('write/', BlogPostCreateView.as_view(), name='write'),
    path('post/<int:pk>/',BlogPostDetailView.as_view() , name='blog_post'),
    path('post/<slug:slug>/',BlogPostDetailView.as_view() ,name='blog_post_slug'),
    path('',BlogPostFeedListView.as_view() , name='feed'),
    path('recommended/',RecommendedBlogPostsListView.as_view() , name='recommended'),
    path('<int:pk>/rate/<int:value>/',rate_view,name='rate'),
    path('<int:pk>/comment/', comment_view, name='comment'),
    path('preview/', preview_view, name='preview'),
]