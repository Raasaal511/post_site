from django.urls import path
from . import views
from .services import user_register, user_login

app_name = 'users'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('register/', user_register, name='user_register'),
    path('login/', user_login, name='user_login'),
]
