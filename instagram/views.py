from distutils.command.upload import upload
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import AddComments, Post
from .forms import PostCreate, CommentCreate

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

def edit_post(request, post_id):
    post_id = int(post_id)
    try:
        posts = Post.objects.get(id = post_id)   
        post_form = PostCreate(request.POST or None, instance=posts)
        # post_form = PostCreate(request.POST ,request.FILES )
        
        if post_form.is_valid():
            post_form.save()
            return redirect('index')
        return render(request, 'home/upload_form.html', {'upload_form': post_form})
    except Post.DoesNotExist:
        return redirect('index')

def delete_post(request, post_id):
    post_id = int(post_id)
    try:
        posts = Post.objects.get(id = post_id)
    except Post.DoesNotExist:
        return redirect('index')
    posts.delete()
    return redirect('index')

def comment_post(request):
    comment = CommentCreate()
    if request.method == 'POST':
        comment = CommentCreate(request.POST, request.FILES)
        if comment.is_valid():
            comment.save()
            return redirect('index')
        else:
            return HttpResponse(""" Something went wrong <a href="{{url: 'index}}">Reload</a> """)

    else:
        return render(request, 'home/comment_form.html', {'comment_form': comment})

def delete_comment(request, comment_id):
    comment_id = int(comment_id)
    try:
        comment = AddComments.objects.get(id = comment_id)
    except AddComments.DoesNotExist:
        return redirect('index')
    comment.delete()
    return redirect('index')
