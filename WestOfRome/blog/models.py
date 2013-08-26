from django.db import models
from django.contrib import admin

class BlogPost(models.Model): 
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    blog_category = models.PositiveSmallIntegerField()

admin.site.register(BlogPost)
