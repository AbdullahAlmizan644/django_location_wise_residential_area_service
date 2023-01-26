from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages

# Create your views here.

def user_login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "Welcome to user dashboard")
            return redirect("/user_dashboard")
            
        else:
            messages.error(request, "wrong username or password")
            return redirect("/")
    return render(request, "user_auth/login.html")



def user_logout(request):
    logout(request)
    return redirect("/")



def user_signup(request):
    if request.method=="POST":
        first_name=request.POST["f_name"]
        last_name=request.POST["l_name"]
        email=request.POST["email"]
        username=request.POST["username"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]

        old_user=User.objects.get(username=username)

        if old_user:
            messages.error(request, "Username already exists")
            return redirect("/user_signup")

        if len(username)<4:
            messages.error(request, "Username must be greater than 4 digits")
            return redirect("/user_signup")

        if len(email)<4:
            messages.error(request, "Email must be greater than 4 digits")
            return redirect("/user_signup")

        if len(pass1)<8:
            messages.error(request, "Password must be greate than 8 digit")
            return redirect("/user_signup")

        if pass1!=pass2:
            messages.error(request, "Password doesn't match")
            return redirect("/user_signup")

        else:
            user=User.objects.create_user(username,email,pass1)
            user.first_name=first_name
            user.last_name=last_name
            user.save()
            messages.success(request,"your registration complete")
            return redirect("/")
    return render(request, "user_auth/register.html")


def user_dashboard(request):
    if request.user.is_authenticated:
        user=User.objects.get(username=request.user)
        print(request.user)
        return render(request, "user_auth/user_dashboard.html")

    else:
        return redirect("/user_login")


