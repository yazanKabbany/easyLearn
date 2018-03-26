from django.conf.urls import url
from django.urls import path

from . import views
from blog.views import follow_view, unfollow_view 

app_name = 'users'
urlpatterns = [
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    path(
        '<slug:username>/follow/',
        follow_view,
        name='follow'
    ),
    path(
        '<slug:username>/unfollow/',
        unfollow_view,
        name='unfollow'
    )
    
]
