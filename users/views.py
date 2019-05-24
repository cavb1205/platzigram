from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView

from users.models import Profile
from users.forms import SignupForm







def sing_in(request):
    """view user login"""

    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error':'invalid user autenticated'})

    return render(request, 'users/login.html')


def sing_up(request):
    """user signup"""

    if request.method == 'POST':
        
        form = SignupForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('users:login')
    else:
            form = SignupForm()

    return render(
        request, 
        template_name='users/singup.html',
        context={'form':form}
    )

        
        
    


def logout_view(request):
    """view logout user"""

    logout(request)
    return redirect('users:login')