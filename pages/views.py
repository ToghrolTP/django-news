from django.views.generic import (ListView,
                                  DetailView,)
from django.views.generic.edit import (CreateView,
                                       UpdateView,
                                       DeleteView,)
from django.urls import reverse_lazy
from .models import Post


class HomeListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ["title", "body"]


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")