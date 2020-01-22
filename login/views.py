from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.core.cache import cache
from .models import *
from .utils import *
from .exceptions import *
from .user import *
from login.forms import *


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        try:
            if form.is_valid():
                cd = form.cleaned_data
                try:
                    user_id = User.objects.get(email=cd['email'])
                except User.DoesNotExist:
                    raise AuthFailureException()

                if user_id.pw == encrypt(cd['pw'] + user_id.salt):  # check validation of account
                    if user_id.is_active is False:
                        raise NotEmailAuthException()
                    response = render(request, 'login/login.html', {'name': user_id.name, 'email': user_id.email})
                    token = create_token(user_id)
                    cache.set(token, user_id.pk, timeout=EXPIRE_HOUR)
                    response.set_cookie(key='token', value=token, httponly=True)
                    return response
                else:
                    raise AuthFailureException()
        except AuthFailureException:
            return render(request, 'login/index.html', {'alert': '로그인 실패'})
        except NotEmailAuthException:
            if email_valid(user_id, request.get_host()):
                return render(request, 'login/index.html', {'alert': '토큰 만료로 인증 메일 재송신'})
            else:
                return render(request, 'login/index.html', {'alert': '인증되지 않은 계정입니다.'})
    else:
        token = request.COOKIES.get('token', None)
        if token is None:
            return render(request, 'login/index.html', {})
        else:
            decoded = is_valid_token(token)
            if decoded is not None:
                user_id = User.objects.get(pk=decoded)
                return render(request, 'login/login.html', {'name': user_id.name, 'email': user_id.email})
            else:
                return render(request, 'login/index.html', {'alert': '토큰이 만료되었습니다.'})


def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                User.objects.get(email=cd['email'])
                return render(request, 'login/register.html', {'message': '이미 존재하는 이메일입니다.'})
            except User.DoesNotExist:
                new_user = User()
                account_register(new_user, cd)
                email_valid(new_user, request.get_host())
                return render(request, 'registration/send_auth_email.html', {'email': new_user.email})
    return render(request, 'login/register.html', {})


def logout(request):
    token = request.COOKIES.get('token', None)
    if token is None:
        return redirect('index')
    else:
        cache.delete(request.COOKIES['token'])
        response = redirect('index')
        response.delete_cookie('token')
        return response


def email_auth(request, uid64, token):
    cache_token = cache.get(uid64)
    if token == cache_token:
        cache.delete(uid64)
        user_id = User.objects.get(pk=force_text(urlsafe_base64_decode(uid64)))
        user_id.is_active = True
        user_id.save()
        return redirect('index')
    else:
        return HttpResponse('만료된 세션입니다.')
