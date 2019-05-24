from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from posts.models import Post
from posts.forms import PostForm




class PostsFeedView(ListView):
    """show list posts order_by -created posts"""

    model = Post
    context_object_name = 'Posts'
    template_name = 'posts/feed.html'
    ordering = ('-created')
    


class PostDetailView(DetailView):
    """show detail posts"""

    model = Post
    slug_field = 'title'
    slug_url_kwarg = 'title'
    template_name = 'posts/detail.html'
    




def new_post(request):
    """create new post"""

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()

    return render(request=request, 
        template_name='posts/new.html', 
        context={'form':form, 
            'user':request.user, 
            'profile': request.user.profile})
