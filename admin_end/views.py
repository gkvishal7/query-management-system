import smtplib
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from user_end.models import query
from django.contrib.auth import logout
from accounts.models import user
from django.core.mail import send_mail
@login_required(login_url='/login/')
def admin(request):
    if request.method=="GET":
        query_list=list(query.objects.filter(query_status=False).values())
        for i in query_list:
            i['user_details_id']=user.getusername(user.objects.get(id=i.get("user_details_id"))).capitalize()
        return render(request,"admin_end/admin_end.html",{'query_list':query_list})
    if request.method=="POST":
        if 'acknowledgement' in request.POST:
            queryid=(request.POST['queryid'])
            querytochange=query.objects.get(id=queryid)
            querytochange.query_status=True
            user_id=querytochange.user_details_id
            querytochange.save()
            emailname=user.getusername(user.objects.get(id=user_id)).capitalize()
            emailid=user.objects.get(id=user_id)
            emailquerydate=querytochange.query_date.strftime('%d/%m/%Y')
            emailtext="Dear "+emailname+","+"\nThis is to confirm that we have seen your query dated on "+emailquerydate+".\nWe assure you that the query will be resolved ASAP. \nRegards  "
            emailsubject="Acknowledgement for your query"
            send_mail(emailsubject, emailtext, 'querymanagementsystem@software', [emailid])
            query_list=list(query.objects.filter(query_status=False).values())
            for i in query_list:
                i['user_details_id']=user.getusername(user.objects.get(id=i.get("user_details_id"))).capitalize()
            return render(request,"admin_end/admin_end.html",{'query_list':query_list})
        elif 'viewquery' in request.POST:
            queryid=int((request.POST['queryid']))
            querydata=list(query.objects.filter(id=queryid).values())
            return render(request,"admin_end/admin_view_description.html",{'query_list':querydata})
def logout_admin(request):
    logout(request)
    return redirect("/")
def history(request):
    query_list=list(query.objects.all().values())
    for i in query_list:
            i['user_details_id']=user.getusername(user.objects.get(id=i.get("user_details_id"))).capitalize()
    return render(request,"admin_end/admin_end_history.html",{'query_list':query_list})
    