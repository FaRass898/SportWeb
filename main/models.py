from django.db import models

class Slogan(models.Model):
    text = models.CharField(max_length=255)

class YouTubeVideo(models.Model):
    url = models.URLField()

class PopularProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
