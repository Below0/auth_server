from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets

from .models import *
from .serializers import UserSerializer
from .utils import *
from .exceptions import *

# Create your views here.
from login.forms import *


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user_id = cache.get(cd['email'])
            try:
                if user_id:
                    print('캐쉬에 존재')
                    user_id = user_id.decode('utf-8')
                    user_dict = dict(json.loads(user_id))
                    pw = user_dict['pw']
                    email = user_dict['email']
                    name = user_dict['name']
                else:
                    try:
                        user_id = User.objects.get(email=cd['email'])
                    except User.DoesNotExist:
                        raise AuthFailureException()
                    print('DB에 존재')
                    pw = user_id.pw
                    email = user_id.email
                    name = user_id.name
                    user_id.save_into_cache()
                if pw == encrypt(cd['pw']):
                    return render(request, 'login/login.html', {'name': name, 'email': email})
                else:
                    raise AuthFailureException()
            except AuthFailureException:
                return render(request, 'login/index.html', {'message': '로그인 실패'})

    else:
        return render(request, 'login/index.html', {})


def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                User.objects.get(email=cd['email'])
                return HttpResponse('CANNOT REGISTER')
            except User.DoesNotExist:
                new_user = User()
                new_user.register(cd)
                return HttpResponse('CAN REGISTER')
    return render(request, 'login/register.html', {})


def logout(request):
    return render(request, 'login/index.html', {})