from django.shortcuts import render

from post.models import Post
from users.models import Profile


def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    user_posts = Post.objects.filter(author_id=profile.user.id)

    context = {
        'profile': profile,
        'user_posts': user_posts,
    }
    return render(request, 'main/profile.html', context)
