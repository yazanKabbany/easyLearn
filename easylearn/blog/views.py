from django.shortcuts import render
from django.views.generic import CreateView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import BlogPostForm

# Create your views here.


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    form_class = BlogPostForm
    template_name = "blog/write.html"
    success_url = ''

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super(BlogPostCreateView, self).form_valid(form)
        