from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """User model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('List name', max_length=50)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
