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
    template_name = "blog/post_details.html"
    pk_url_kwarg = 'pk'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True



class BlogPostFeedListView(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = "blog/post_feed.html"
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        followed_ids = user.followed.all().values_list('followed', flat=True)
        queryset = BlogPost.objects.filter(writer__in=followed_ids)
        return queryset

class RecommendedBlogPostsListView(LoginRequiredMixin, ListView):
    model = BlogPost
    #template_name = "TEMPLATE_NAME"


class UserPostsListView(LoginRequiredMixin, ListView):
    model = BlogPost
    #template_name = "TEMPLATE_NAME"
