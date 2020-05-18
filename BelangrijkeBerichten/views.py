from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from users.models import Follow, Profile
import sys
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def is_users(post_user, logged_user):
    return post_user == logged_user



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content']
    template_name = 'BelangrijkeBerichten/home.html'
    success_url = '/'


