from django.shortcuts import render, redirect
from .models import Blog, Post, Video
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth.forms import authenticate
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
import requests


#@login_required
def home_view(request):
    products = Blog.objects.all()
    return render(request, 'app/index.html', {'products': products})


#@login_required
def video_view(request):
    videos = Video.objects.all()
    return render(request, 'app/videos.html', {
        'videos': videos,
    })
    
    
def post(request):
    posts = Post.objects.filter()
    return render(request, 'app/posts.html', {'posts': posts})


def signup(request):
    form = SignupForm()
    
    if request.method == "POST":
         form = SignupForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('login')
         
    return render(request, 'app/signup.html', {'form': form})   
    
      
def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if User is not None:
                auth.login(request, user)
                return redirect('home')
         
    return render(request, 'app/login.html', {'form': form})
     

def logout(request):
    auth.logout(request)
    return redirect('/login/')

