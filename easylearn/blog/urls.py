from django.urls import include, path
from .views import BlogPostCreateView
app_name = 'blog'

urlpatterns = [
    path('write', BlogPostCreateView.as_view(), name='write')
]