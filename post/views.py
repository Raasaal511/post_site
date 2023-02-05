from django.shortcuts import render

from .models import Post, Category


def home(request):
    posts = Post.objects.select_related('category').all()

    return render(request, 'main/home.html', {'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, 'main/post_detail.html', {'post': post})
