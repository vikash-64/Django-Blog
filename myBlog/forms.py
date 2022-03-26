from django import forms
from . models import Blog 
from . models import Contact 
from django import forms
from .models import *




class Blog_Form(forms.ModelForm):
    ImgLink = forms.URLField( )
    class Meta :
        
        model = Blog 
        fields = (  'title' , 'description' , 'ImgLink' , )

 
class Edit_Blog(forms.ModelForm):
    
    class Meta :
        
        model = Blog
        fields = ( 'title' , 'description' )
        
        
class Contact_form(forms.ModelForm):
    

    
    class Meta :
        
        model = Contact 
        fields = ('first_name' , 'last_name' , 'email' , 'phone' , 'message')