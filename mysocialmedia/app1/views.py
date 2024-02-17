from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import MainCatogory, ProdCatogory, Products, CartItem
# Create your views here.

def home(request):
    return render(request,'home.html')

def reels(request):
    return render(request,'home1.html')

def usersignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        if password1 == password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username alreadt exists!!!')
                print("already have")
                return redirect('SuperMarket1:user_signup')
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                return redirect('SuperMarket1:user_login')
        else:
            print('wrong password')
    return render(request,'signup.html')

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass1')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('app1:all_products')
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect('app1:user_login')
    return render(request,'login.html')

def userlogout(request):
    logout(request)
    return redirect('app1:user_login')

def explore(request):
    return render(request,'explore.html')

def addpost(request):
    return render(request,'addpost.html')

def addreels(request):
    return render(request,'addreel.html')

def followeduserprofile(request):
    return render(request,'followeduserprofile.html')

def myprofile(request):
    return render(request,'myprofile.html')

def userprofile(request):
    return render(request,'userprofile.html')

