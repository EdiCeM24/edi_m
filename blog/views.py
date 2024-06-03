from django.shortcuts import render, redirect
from .models import Blog, Post, Video
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required


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
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignupForm()    
    
    return render(request, 'app/signup.html', {
        'form': form,
    })   
    
    
    
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
    return render(request, 'app/login.html')
     



