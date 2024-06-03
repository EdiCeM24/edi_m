from django.contrib import admin
from .models import Blog, Post, Video


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'slug', 'publish_date', 'author', 'content', 'status')


class VideoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image', 'publish_date', 'content', 'slug', 'author')
    
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'publish_date')
    
     
admin.site.register(Post, PostAdmin)

admin.site.register(Video, VideoAdmin)

admin.site.register(Blog, BlogAdmin)


