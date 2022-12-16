from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#importing custom user model and query model
from accounts.models import user
from .models import query
#pytz for handling time-zone
import pytz
#for getting current time
from datetime import datetime

#Only Logged in User can access the view
@login_required(login_url='/')
def user_view(request):
    if request.method=="POST":
        #Getting data from POST request
        query_date=request.POST['date']
        query_date = datetime.strptime(query_date, '%m/%d/%Y').date()
        query_title=request.POST['query_title']
        query_data=request.POST['query_description']
        query_time=datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%H:%M:%S")
        
        #Creating query model object for storing query in DB
        query_object=query(query_title=query_title,query_description=query_data,query_date=query_date,query_time=query_time,user_details=request.user)
        query_object.save()
    #send_mail('subject', 'body of the message', 'noreply@bottlenose.co', ['vishwanathnaryanan29@gmail.com'])
    return render(request,"user_end/user_end.html")