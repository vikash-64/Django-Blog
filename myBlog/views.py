from django.shortcuts import render , redirect
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate, login , update_session_auth_hash
from django.contrib import messages 
from django.contrib.auth import logout
from . models import Blog
from .forms import Blog_Form
from .forms import Edit_Blog
from .forms import Contact_form
from django.forms import ModelForm
from django.conf import settings
from django.core.mail import send_mail



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
            subject = "About Registration"
            message = f'Hi {uname} You has been register successfully on Code Blog' 
            email_form = 'vikash400001@gmail.com'
            rec_list = [email,]
            send_mail(subject, message, email_form, rec_list)
            messages.success(request, "Registerd Successfully")
            return redirect('/')
     
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
            messages.warning(request, "Incorrect login credentials i.e. userHandle/email or password!")
            return redirect("/user_login")
    return render(request, 'login.html')  

def user_logout(request): 
    
    logout(request)
    return redirect("/")

def post_blog(request):
    form = Blog_Form(request.POST)
    if request.method == 'POST' :

        
        if form.is_valid() :
            post = form.save(commit=False)
            post.user_id = request.user
            print(post.ImgLink)
            post.save()
            messages.success(request, "Post Has been Submited Successfully ")
            
            return redirect('/')
            
        else:
            form = Blog_Form()
    
    return render(request, 'post_blog.html', {'form' : form})

    
        
        
    
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
    
    
    
def contact_form(request):
    
    form = Contact_form()
    
    if request.method == 'POST' :
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for contact")
            return redirect('/')
   
    return render(request, 'contact_form.html' , {'form':form} )
  

def change_password(request):
    
    
    
    if request.method == 'POST' :
        
       oldpsw =  request.POST.get('oldpassword')
       newpsw = request.POST.get('newpassword')
       u = User.objects.get(username=request.user.username)
       
       if u.check_password(oldpsw):
           u.set_password(newpsw)
           u.save()
           update_session_auth_hash(request, request.u)
           messages.success(request, "Password has been changed successfully")
           return redirect('/')
       else:
           messages.success(request, "Invalid Password")
           return redirect('/change_password')
           
        
    
    return render(request, 'change_password.html')



