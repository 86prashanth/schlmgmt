from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('register/',Register,name='register'),
    path('existing/',Existing,name='registered'),
    path('searchstudent/',searchform,name='search'),
    path('dropout/',dropout,name='dropout'),
    path('about/',about,name='about'),
]
