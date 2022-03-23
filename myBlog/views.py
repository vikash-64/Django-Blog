from django.shortcuts import render , redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login
from django.contrib import messages 
from django.contrib.auth import logout
from . models import Blog
from .forms import Edit_Blog



# Create your views here.

def index(request):
    
    blog = Blog.objects.all()
    context = {'blogs' : blog}
    return render(request, 'home.html' , context) 

def register(request):
    
    if request.method == 'POST':
        
        uname =  request.POST.get('uname')
        email =  request.POST.get('email')
        psw =  request.POST.get('psw')
        psw2 =  request.POST.get('psw2')
        if  User.objects.filter(username=uname).exists() :
            messages.warning(request, "Username already exist")
            return redirect('register')
        elif psw != psw2 :
            messages.warning(request, "Password not match")
            return redirect('register')
        elif  User.objects.filter(email=email).exists() :
            messages.warning(request, "email already exist")
            return redirect('register')
        else:
            user = User.objects.create_user( username=uname , email=email, password=psw)
            user.save()
            messages.success(request, "Registerd Successfully")
            return redirect('user_login')
     
    return render(request, 'register.html')

def user_login(request):
    
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request , user)
            return redirect('/')
        else:
            messages.warning(request, "Invalid credentials")
            return redirect("/user_login")
    return render(request, 'login.html')  

def user_logout(request): 
    
    logout(request)
    return redirect("/")

def post_blog(request):
    
    if request.method == 'POST' :
        title = request.POST.get('title')
        description = request.POST.get('subject')
        img = request.FILES['image']
        blog = Blog(title= title , description=description , user_id=request.user , cover=img)
        blog.save()
        messages.success(request, "Post Has been Submited Successfully ")
        return redirect('/post_blog')
    
        
        
    
    return render(request, 'post_blog.html')    

def blog_detail(request , id):
    
    blog = Blog.objects.get(id=id)
    context = {'blog':blog}
    return render(request, 'blog_detail.html' , context)

def delete(request , id):
    
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.success(request, "Post Has Been Deleted")
    return redirect('/')

def edit(request , id):
    blog = Blog.objects.get(id=id)
    editblog = Edit_Blog(instance=blog)
    if request.method== 'POST':
        form = Edit_Blog(request.POST , instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'POST has been Updated')
            return redirect('/')
    return render(request, 'edit_blog.html' , {'edit_blog':editblog})
    
    
    
    