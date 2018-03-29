from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseBadRequest

from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import BlogPostForm
from blog.models import BlogPost, Following, Rating, Comment
from easylearn.users.models import User

from markdown import markdown


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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        user = self.request.user
        try:
            rating = Rating.objects.get(rater=user, post=self.object)
        except Rating.DoesNotExist:
            rating_val = -1
        else:
            rating_val = rating.value
        context['rating'] = rating_val
        return context


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


@login_required
def follow_view(request, username):
    curent_user = request.user
    other_user = User.objects.get(username=username)
    if Following.objects.filter(follower=curent_user, followed=other_user).exists():
        return HttpResponseRedirect(other_user.get_absolute_url())

    following = Following(follower=curent_user, followed=other_user)
    following.save()
    return HttpResponseRedirect(other_user.get_absolute_url())


@login_required
def unfollow_view(request, username):
    curent_user = request.user
    other_user = User.objects.get(username=username)
    following = Following.objects.filter(follower=curent_user, followed=other_user)
    if not following.exists():
        return HttpResponseRedirect(other_user.get_absolute_url())

    following.delete()
    return HttpResponseRedirect(other_user.get_absolute_url())

@login_required
def rate_view(request, pk, value):
    user = request.user
    rating = None
    try:
        rating = Rating.objects.get(rater=user, post=pk)
    except Rating.DoesNotExist:
        rating = Rating(rater=user, post=BlogPost.objects.get(pk=pk))
    rating.value = value
    rating.save()
    return redirect(BlogPost.objects.get(pk=pk))

@login_required
def comment_view(request, pk):
    user = request.user
    post = get_object_or_404(BlogPost, pk=pk)
    try:
        text = request.POST['text']
    except KeyError:
        return HttpResponseBadRequest()
    comment = Comment(writer=user, post=post, text=text)
    comment.save()
    return redirect(post)

@login_required
def preview_view(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    try:
        text = request.POST['text']
    except KeyError:
        return HttpResponseBadRequest()
    html_text = markdown(text)
    return render(request, 'blog/preview.html',{'text':html_text})