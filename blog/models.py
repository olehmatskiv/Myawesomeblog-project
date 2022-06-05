from django.db import models

# Create your models here.

class Post(models.Model):
    title_post = models.CharField(max_length = 50)
    date_post = models.DateTimeField()
    text_post = models.TextField(max_length=300)
    image_post = models.ImageField(upload_to="post_images/")

    def get_summary(self):
        return self.text_post[:70]

    def __str__(self):
        return self.title_post
