from django.urls import path
from .views import (HomeListView,
                    PostDetailView,)

urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("new/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
]
