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
        email=request.POST['emailid']
        passwd=request.POST['password']
        user=auth.authenticate(request,email=email,password=passwd)
        print(user.is_superuser)
        if(user is not None):
            if user.is_superuser:
                auth.login(request,user)
                return redirect("/admin_end/")
            else: 
                    auth.login(request,user)
                    print("Success")
                    return redirect("/querysubmit/")
        else:
            print("Failed")
            messages.error(request,"Invalid Credentials")
            return redirect("/")   
    else:
        return redirect("/")

#Register Method
def register(request):
    if(request.method=="POST"):
        name=request.POST['username']
        email=request.POST['emailid']
        passwd=request.POST['password1']
        confirm_passwd=request.POST['password2']

        if(passwd==confirm_passwd):
            if user.objects.filter(username=name).exists():
                messages.error(request,"Username already Exists")
                return redirect("/")
            elif user.objects.filter(email=email).exists():
                messages.error(request,"Already Registered with this mail ID")
                return redirect("/")
            else :
                 userobj=user.objects.create_user(username=name,email=email,password=passwd)
                 userobj.save()
                 messages.success(request,"Successfully Created")
                 return redirect("/")
        else:
            messages.error(request,"Password Not Matching")
            return redirect("/")
    else:
        return redirect("/")
