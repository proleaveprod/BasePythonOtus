from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('about/', views.about, name='about'),
    
    path('add_post1/', views.add_post1, name='add_post1'),
    path('add_post2/', views.add_post2, name='add_post2'),
]
