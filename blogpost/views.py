from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages



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
def delete_blog(request):
    pass
def create_blog(request):
    pass
def update_blog(request):
    pass
def show_blogs(request):
    return render

def index(request):
    return render(request,'body.html')