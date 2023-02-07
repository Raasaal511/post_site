from django.shortcuts import redirect


def save_comment(request, form, post):
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()

        return redirect('post_detail', post.slug)
