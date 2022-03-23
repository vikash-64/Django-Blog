from django.contrib import admin
from django.urls import path , include 
from myBlog import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    
    path('Blog', post_blog, name = 'Blog'),
    path('' , views.index , name = 'index'),
    path("register/", views.register, name="register"),
    path("user_login/", views.user_login, name="user_login"),
    path("user_logout/", views.user_logout, name="user_logout"),
    path("post_blog/", views.post_blog, name="post_blog"),
    path('blog_detail/<int:id>' , views.blog_detail ,name='blog_detail'),
    path('delete/<int:id>' , views.delete ,name='delete'),
    path('edit/<int:id>' , views.edit ,name='edit')
    
]
