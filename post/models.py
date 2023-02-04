from django.db import models


class Post(models.Model):
    title = models.CharField('Title', max_length=150)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    discription = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField('Title', max_length=150)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
