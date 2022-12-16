from django.urls import path
from . import views

urlpatterns=[
    path('admin_end/',views.admin,name='admin'),
    path('logout/',views.logout_admin,name=''),
    path('admin_end/history/',views.history,name=''),

]