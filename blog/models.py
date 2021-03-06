from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=1000)
    categorie = models.TextField(max_length=100, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.author.username + ": " + self.title +self.content

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post_connected=self).count()

class Belangrijkbericht(models.Model):
    content = models.TextField(max_length=1000)
    categorie = models.TextField(max_length=100, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.author.username + ": " + self.content

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post_connected=self).count()



class Comment(models.Model):
    content = models.TextField(max_length=800)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.author.username + ": " + self.content
