from django.shortcuts import render
from pages.models import Post
from django.views.generic import ListView, DetailView

class PostsListView(ListView):
      model = Post

class PostDetailView(DetailView):
      model = Post
# Create your views here.
