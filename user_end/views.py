from django.shortcuts import render
from django.core.mail import send_mail

from django.http import HttpResponse
# Create your views here.
def user_view(request):
    
    #send_mail('subject', 'body of the message', 'noreply@bottlenose.co', ['vishwanathnaryanan29@gmail.com'])
    return render(request,"user_end/user_end.html")