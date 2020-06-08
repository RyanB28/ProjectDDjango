from django.contrib import admin
from blog.models import Belangrijkbericht, Comment, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', )
    list_filter = ['date_posted']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', )
    list_filter = ['date_posted']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Belangrijkbericht)
