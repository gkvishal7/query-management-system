from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user_end.models import query
from accounts.models import user
@login_required(login_url='/login/')
def admin(request):
    if request.method=="GET":
        query_list=list(query.objects.filter(query_status=False).values())
        for i in query_list:
            i['user_details_id']=user.getusername(user.objects.get(id=i.get("user_details_id"))).capitalize()
        return render(request,"admin_end/admin_end.html",{'query_list':query_list})
    if request.method=="POST":
        queryid=(request.POST['queryid'])
        querytochange=query.objects.get(id=queryid)
        querytochange.query_status=True
        querytochange.save()
        query_list=list(query.objects.filter(query_status=False).values())
        for i in query_list:
            i['user_details_id']=user.getusername(user.objects.get(id=i.get("user_details_id"))).capitalize()
        return render(request,"admin_end/admin_end.html",{'query_list':query_list})
        