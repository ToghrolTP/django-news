from django.urls import path
from .views import (HomeListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView)

urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name = "post_new"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name = "post_update")
]
