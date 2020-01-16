from django.urls import path
from rest_framework import routers
from django.conf.urls import url, include

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('register/', register, name="register"),
    path('logout/', logout, name="logout"),
]
