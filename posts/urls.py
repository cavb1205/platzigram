from django.urls import path

from posts import views

urlpatterns = [
    #url for posts
    path('', views.PostsFeedView.as_view(), name='feed'),
    path('<slug:title>',views.PostDetailView.as_view(), name='detail'),
    path('new/', views.new_post, name='new_post'),

]
