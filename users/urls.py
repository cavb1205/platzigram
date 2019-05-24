from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
     #url for users
    path('login_view/', views.sing_in, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('singup/', views.sing_up, name='singup'),
    path('<str:username>/', TemplateView.as_view(template_name='users/detail.html'), name='detail'),
  
]
