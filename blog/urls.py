from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    ImportantPostCreateView,
    TagListView)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/del/', PostDeleteView.as_view(), name='post-delete'),
    path('importantpost/new', ImportantPostCreateView.as_view(), name='import-post'),
    path('tag/<slug:slug>/', TagListView.as_view(), name='tagged'),
    path('base_layout', PostListView.as_view(), name='base_layout'),
]