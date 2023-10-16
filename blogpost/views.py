from django.shortcuts import  get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from blogpost import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime


def auth(request):
    return render(request, 'auth_form.html')
def signin(request):
    if(request.method == "POST"):
        username = request.POST["username"]
        password = request.POST["password"]
        if username=='' or password=='' :
            messages.error(request,"Make sure to fill all the boxes !!")
            return redirect('register')
        else:
            user = authenticate(username=username, password=password)
            if(user is not None):
                login(request,user)
                return redirect("index")
            else:
                messages.error(request, "Invalid Credentail")
                return redirect("auth")
                                        
def register(request):
    if(request.method == "POST"):
         username = request.POST["username"]
         email = request.POST["email"]
         password = request.POST["password"]
         if username=='' or email =='' or email=='' or password=='' :
            messages.error(request,"Make sure to fill all the boxes !!")
            return redirect('register')
         else:
             if(User.objects.filter(username=username).exists()):
                 messages.error(request,"User With this username already exists" )
                 return redirect('register')

             else:
                 new_user = User.objects.create_user(username=username, email=email,  password=password)
                 new_user.save()
                 messages.success(request,"User created now signin" )
                 return redirect("index")
                   
    
    else:
        return render(request, 'signup_form.html')

def signout(request):
    logout(request)
    return redirect('index')
def delete_blog(request, id):
    blog = get_object_or_404(models.Blog, id=id)  # Get the blog entry or raise a 404 error if not found
    blog.delete()  # Delete the blog entry
    messages.success(request, "Blog Deleted Successfully")
    return redirect('index')

    
    pass
def create_blog(request):
    if(request.method == "POST"):
        title = request.POST["title"]
        body = request.POST["body"]
        if(title == "" or body == ""):
            messages.error(request,"no title or body provider" )
        else:
            new_blog = models.Blog.objects.create(author=request.user, title = title, body= body)
            messages.success(request,"Blog Created Successfully" )
            return redirect('index')

    return render(request,'add_blog.html')

@login_required
def update_blog(request, id):
   blog = models.Blog.objects.get(id=id)
   if(request.method == "POST"):
       new_title = request.POST["title"]
       new_body = request.POST["body"]
       blog.title = new_title
       blog.body = new_body
       blog.post_date = datetime.datetime.strftime(datetime.date.today(),'%Y-%m-%d')
       blog.save()
       messages.success(request,"Blog Updated Successfully" )

       return redirect('index')
   return render(request, 'update_blog.html', {"blog":blog})
    

def show_blogs(request):
    return render(request, 'body.html')

def index(request):
    if(request.user.is_authenticated):
        data = models.Blog.objects.filter(author = request.user).all()
        return render(request,'body.html', {"data":data})
    return render(request,'body.html')