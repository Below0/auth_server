from django.urls import path
from rest_framework import routers
from django.conf.urls import url, include

from .views import *
urlpatterns = [
    path('', index, name="index"),
    path('register/', register, name="register"),
    path('register/<str:uid64>/<str:token>', email_auth, name="email_auth"),
    path('logout/', logout, name="logout"),
]
