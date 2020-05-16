from django.contrib import admin
from blog.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', )
    list_filter = ['date_posted']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
