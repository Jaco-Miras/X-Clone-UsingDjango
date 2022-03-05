from django.db import models
from django.utils import timezone

class Post(models.Model):
    image = models.ImageField()
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


    