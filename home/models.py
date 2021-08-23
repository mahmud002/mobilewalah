from django.db import models
from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import User,auth


# Create your models here.

class Blog(models.Model):
   
    
    title=models.TextField(max_length=30, blank=True)
    intro=models.TextField(max_length=100, blank=True)
    post=models.TextField(max_length=2000, blank=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="home/images", default="",null=True, blank=True)
    
