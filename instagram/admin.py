from django.contrib import admin
from .models import AddComments, Post

admin.site.register(Post)
admin.site.register(AddComments)

