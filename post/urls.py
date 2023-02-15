from django.urls import path
from . import views
from . import services as sc


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', sc.post_create, name='post_create'),

    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/update/', sc.post_udpate, name='post_update'),
    path('<slug:slug>/delete/', sc.post_delete, name='post_delete'),
]
