from django.shortcuts import render,redirect
from django.contrib.auth .models import auth
from django.contrib import messages
from .models import user


def home(request):
    return render(request,'accounts/home.html')

def login(request):
    print('hello')
    if(request.method=="POST"):
        email=request.POST['emailid']
        passwd=request.POST['password']
        print("Email : ",email)
        user=auth.authenticate(request,email=email,password=passwd)
        if(user is not None):
            auth.login(request,user)
            print("Success")
            print("user login successfully")
            return redirect("/querysubmit/")
        else:
            print("Failed")
            messages.error(request,"Invalid Credentials")
            return redirect("login")
    else:
        return render(request,'accounts/login.html')

def register(request):
    if(request.method=="POST"):
        name=request.POST['name1']
        email=request.POST['email_ID']
        passwd=request.POST['password1']
        confirm_passwd=request.POST['password2']

        if(passwd==confirm_passwd):
            if user.objects.filter(username=name).exists():
                messages.error(request,"Username already Exists")
                return redirect("register")
            elif user.objects.filter(email=email).exists():
                messages.error(request,"Already Registered with this mail ID")
                return redirect("register")
            else :
                 userobj=user.objects.create_user(username=name,email=email,password=passwd)
                 userobj.save()
                 return redirect("/login")
        else:
            messages.error(request,"Password Not Matching")
            return redirect("register")
    else:
        return render(request,'accounts/register.html')
