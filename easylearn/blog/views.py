from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import BlogPostForm
from blog.models import BlogPost
# Create your views here.


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    form_class = BlogPostForm
    template_name = "blog/write.html"
    success_url = ''

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super(BlogPostCreateView, self).form_valid(form)


class BlogPostDetailView(LoginRequiredMixin, DetailView):
    model = BlogPost
    #template_name = ""
    pk_url_kwarg = 'pk'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True



class BlogPostFeedListView(LoginRequiredMixin, ListView):
    model = BlogPost
    #template_name = "TEMPLATE_NAME"


class RecommendedBlogPostsListView(LoginRequiredMixin, ListView):
    model = BlogPost
    #template_name = "TEMPLATE_NAME"


class UserPostsListView(LoginRequiredMixin, ListView):
    model = BlogPost
    #template_name = "TEMPLATE_NAME"
