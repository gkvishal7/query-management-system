
from django.urls import path
from . import views
urlpatterns = [
    path('querysubmit/', views.user_view, name='querysubmit'),
]