
from django.conf.urls import patterns, url

from pages.views import PostsListView, PostDetailView

urlpatterns = patterns('',
url(r'^$', PostsListView.as_view(), name='list'),
url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
)
