from django.urls import path

from . import views

urlpatterns = [
    #url for posts
    path('', views.list_posts, name='feed'),
    path('new/', views.new_post, name='new_post'),

]
