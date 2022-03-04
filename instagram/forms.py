from pyexpat import model
from django import forms
from . models import Post

class PostCreate(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'