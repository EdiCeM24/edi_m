from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home-view'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('video_view', views.video_view, name='video-view'),
]
