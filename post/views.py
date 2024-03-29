from django.shortcuts import render

from .forms import CommentForm
from .models import Post
from .services import save_comment


def home(request):
    posts = Post.objects.all().select_related('author', 'category').\
        values('author__username', 'title', 'category__title', 'discription',
               'create_at', 'slug')
    return render(request, 'main/home.html', {'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = post.comments.all()
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        save_comment(request, form, post)  # checked that the form is valid and will save the form

    context = {
        'post': post,
        'comments': comments,
        'form': form
    }

    return render(request, 'main/post_detail.html', context=context)
