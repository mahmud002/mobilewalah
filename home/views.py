from home.form import BlogForm
from django.shortcuts import render

from django.forms.widgets import NullBooleanSelect
from django.shortcuts import render ,HttpResponse,redirect
from .models import *

from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
import datetime

# Create your views here.
def index (request):
    data=Blog.objects.all()

    
    return render(request,'home.html',{'data':data})


def profile (request):
    

    
    return render(request,'profile.html')



def create_blog(request):
        form=BlogForm()
        if request.method =='POST':
            form=BlogForm(request.POST,request.FILES)
            
            if form.is_valid():
                
                form.save()
               
            return redirect('blog')
        return render(request,'blog_form.html',{'form':form})
    


