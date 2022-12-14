from django.shortcuts import render,redirect
from django.contrib.auth .models import auth
from django.contrib import messages
from .models import user

#Default Page when visiting
def home(request):
    return render(request,'accounts/home.html')

#Login Method
def login(request):
    if(request.method=="POST"):
        if request.user.is_superuser:
            print("hello")
        else:
            email=request.POST['emailid']
            passwd=request.POST['password']
            user=auth.authenticate(request,email=email,password=passwd)
            if(user is not None):
                auth.login(request,user)
                print("Success")
                return redirect("/querysubmit/")
            else:
                print("Failed")
                messages.error(request,"Invalid Credentials")
                return redirect("login")
    else:
        return render(request,'accounts/login.html')

#Register Method
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
