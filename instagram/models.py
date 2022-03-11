from django.db import models
from django.utils import timezone

class Post(models.Model):
    image = models.ImageField()
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

class AddComments(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, default="")
    body = models.TextField()



    