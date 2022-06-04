from django.db import models

# Create your models here.

class Post(models.Model):
    title_post = models.CharField(max_length = 50)
    date_post = models.DateTimeField()
    text_post = models.TextField(max_length=300)
    image_post = models.ImageField(upload_to="post_images/")
