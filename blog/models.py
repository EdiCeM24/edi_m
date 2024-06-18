from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Blog(models.Model):
    
    class NewManager(models.Model):
        def get_query(self):
            return super().get_queryset().filter(status='publish')
    
    options = {
        ('draft', 'Draft'),
        ('publish', 'Published'),
    }
    
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store', blank=True, null=True)
    slug = models.CharField(max_length=255)
    publish_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=20, choices=options, default='draft')
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()  
    publish_date = models.DateTimeField(default=timezone.now)  
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE, related_name='product')
    
        

class Video(models.Model):
    caption = models.CharField(max_length=255)
    image = models.URLField()
    publish_date = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=50)
    slug = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE, related_name='blog')
    
    def __str__(self) -> str:
        return str(self.caption)
    
    

    
