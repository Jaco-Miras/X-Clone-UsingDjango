from pyexpat import model
from django import forms
from . models import Post,AddComments

class PostCreate(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CommentCreate(forms.ModelForm):
    class Meta:
        model = AddComments
        fields = '__all__'