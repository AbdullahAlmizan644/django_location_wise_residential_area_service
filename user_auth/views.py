from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RentForm,TeacherForm,TutionForm
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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'user_auth/register.html', {'form': form})



def user_dashboard(request):
    if request.user.is_authenticated:
        user=User.objects.get(username=request.user)
        print(request.user)
        return render(request, "user_auth/user_dashboard.html")

    else:
        return redirect("/user_login")



def house_rent_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RentForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.creator = request.user
                instance.save()
                
                messages.success(request,"Post Added Successfully")
                return redirect(user_dashboard)
            else:
                form = RentForm()
             
            return render(request, 'user_auth/house_rent_post.html', {
                'form': form
            })
        
        return render(request, 'user_auth/house_rent_post.html',{
            "c_username":request.user
        })

 

    else:
        return redirect("/user_login")
     


def teacher_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TeacherForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.creator = request.user
                instance.save()
                
                messages.success(request,"Post Added Successfully")
                return redirect(user_dashboard)
            else:
                form = TeacherForm()
             
            return render(request, 'user_auth/teacher_post.html', {
                'form': form
            })
        
        return render(request, 'user_auth/teacher_post.html',{
            "c_username":request.user
        })


    else:
        return redirect("/user_login")
     



def tution_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TutionForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.creator = request.user
                instance.save()
                
                messages.success(request,"Post Added Successfully")
                return redirect(user_dashboard)
            else:
                form = TutionForm()
             
            return render(request, 'user_auth/tution_post.html', {
                'form': form
            })
        
        return render(request, 'user_auth/tution_post.html',{
            "c_username":request.user
        })


    else:
        return redirect("/user_login")
     

