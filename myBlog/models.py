from django.db import models
from django.contrib.auth.models import User
import datetime
from ckeditor.fields import RichTextField


# Create your models here.
 


class Blog(models.Model):
    
    user_id = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True , null=True)
    date = models.DateTimeField(auto_now_add=True , null=True)
    
    ImgLink = models.URLField(max_length = 500 , blank=True , null=True)
    def __str__(self):
        return self.title

class Contact(models.Model): 
    
    first_name = models.CharField(max_length=100 , null=False)
    last_name = models.CharField(max_length=100 , null=False)
    email = models.EmailField(null=False)
    phone = models.IntegerField()
    message = models.TextField(null=False)
    
    def __str__(self):
        return self.email
    
    

    

     
