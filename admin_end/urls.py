from django.urls import path
from . import views

urlpatterns=[
    path('admin_end/',views.admin,name='admin'),
]