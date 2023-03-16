from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from post.models import Post, Category


class TestPost(TestCase):

    def create_post(self):
        user = User.objects.create_user(username='Username')
        category = Category.objects.create(title='Game', slug='game')
        post = Post.objects.create(author=user, title='Post', category=category,
                                   discription='Test post', create_at=timezone.now(), slug='post')
        return post

    def test_post_creation(self):
        post = self.create_post()
        self.assertTrue(isinstance(post, Post))

    def test_post_update(self):
        post = self.create_post()
        response = self.client.patch(reverse('post_update'))

        self.assertEqual(response.status_code, 302)

        post.refresh_from_db()
        self.assertEqual(post.title, 'UpdateTestPost')

    def test_post_delete(self):
        post = self.create_post()
        response = self.client.post(reverse('post_delete', args=(post.slug,)))
        self.assertEqual(response.status_code, 302)

    def test_post_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url(self):
        post = self.create_post()
        response = self.client.get(reverse('post_detail', args=(post.slug,)))

        self.assertEqual(response.status_code, 200)

    def test_post_update_url(self):
        post = self.create_post()
        response = self.client.get(reverse('post_update', args=(post.slug,)))

        self.assertEqual(response.status_code, 200)

    def test_post_delete_url(self):
        post = self.create_post()
        response = self.client.get(reverse('post_delete', args=(post.slug,)))

        self.assertEqual(response.status_code, 200)
