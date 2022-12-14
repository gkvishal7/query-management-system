from django.shortcuts import render,redirect
from django.contrib.auth .models import User,auth
from django.contrib import messages


def home(request):
    return render(request,'accounts/home.html')

def login(request):
    if(request.method=="POST"):
        user_name=request.POST['username']
        passwd=request.POST['password']
        user=auth.authenticate(request,username=user_name,password=passwd)
        if(user is not None):
            auth.login(request,user)
            print("user login successfully")
            return redirect("/")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("login")
    else:
        return render(request,'accounts/login.html')

def register(request):
    # if(request.method=="POST"):
    #     name=request.POST['name1']
    #     email=request.POST['email_ID']
    #     street_name=request.POST['street_name']
    #     area=request.POST['area_name']
    #     city=request.POST['city']
    #     state=request.POST['state']
    #     pincode=request.POST['pincode']
    #     passwd=request.POST['password1']
    #     confirm_passwd=request.POST['password2']

    #     if(passwd==confirm_passwd):
    #         if User.objects.filter(username=name).exists():
    #             messages.error(request,"Username already Exists")
    #             return redirect("register")
    #         elif User.objects.filter(email=email).exists():
    #             messages.error(request,"Already Registered with this mail ID")
    #             return redirect("register")
    #     else:
    #         messages.error(request,"Password Not Matching")
    #         return redirect("register")

    return render(request,'accounts/register.html')
