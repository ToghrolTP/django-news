from django.views.generic import (ListView, DetailView)
from .models import Post


class HomeListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"