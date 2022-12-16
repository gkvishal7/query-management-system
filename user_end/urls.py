
from django.urls import path
from . import views
urlpatterns = [
    path('querysubmit/', views.user_view, name='querysubmit'),
    path('logout/',views.logout_user,name=''),
    path('querysubmit/user_history/',views.history,name=''),

]