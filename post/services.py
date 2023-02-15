from django.shortcuts import redirect, render, get_object_or_404
from django.template.defaultfilters import slugify

from post.forms import PostForm
from post.models import Post


def post_create(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            return redirect('users:profile')

    return render(request, 'main/form/post_create.html', {'form': form})


def post_udpate(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'main/form/post_update.html', {'post': post, 'form': form})


def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        post.delete()
        return redirect('users:profile')

    return render(request, 'main/form/post_delete.html', {'post': post})


def save_comment(request, form, post):
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()

        return redirect('post_detail', post.slug)
