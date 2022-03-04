from distutils.command.upload import upload
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Post
from .forms import PostCreate

def index(request):
    posts = Post.objects.all()
    return render(request, 'home/home.html', {'posts': posts})

def upload(request):
    upload = PostCreate()
    if request.method == 'POST':
        upload = PostCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse(""" Something went wrong <a href="{{url: 'index}}">Reload</a> """)

    else:
        return render(request, 'home/upload_form.html', {'upload_form': upload})

