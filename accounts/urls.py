from django.urls import path
from . import views
#URL Patterns 
urlpatterns=[
    path('',views.home),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
]