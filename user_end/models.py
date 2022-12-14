from django.db import models
from django.conf import settings

#query model for storing query 
class query(models.Model):
    query_info = models.CharField(max_length=1000)
    user_details = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    query_date= models.DateField()
    query_time=models.TimeField()
