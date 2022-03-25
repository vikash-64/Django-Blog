from django.contrib import admin
from django.urls import path , include 
from myBlog import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('Blog', post_blog, name = 'Blog'),
    path('' , views.index , name = 'index'),
    path("register/", views.register, name="register"),
    path("user_login/", views.user_login, name="user_login"),
    path("user_logout/", views.user_logout, name="user_logout"),
    path("post_blog/", views.post_blog, name="post_blog"),
    path('blog_detail/<int:id>' , views.blog_detail ,name='blog_detail'),
    path('delete/<int:id>' , views.delete ,name='delete'),
    path('edit/<int:id>' , views.edit ,name='edit'),
    path('contact_form/' , views.contact_form , name= 'contact_form'),
    path('change_password/' , views.change_password , name= 'change_password'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"), name ='password_reset_complete')

    
]
