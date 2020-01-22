from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.utils.http import *
from django.core.cache import cache

from .utils import *
from .constants import *


def account_register(user, cd):
    user.name = cd['name']
    user.email = cd['email']
    user.salt = create_salt()
    user.pw = encrypt(cd['pw'] + user.salt)
    user.is_active = False
    user.save()


def email_valid(user, domain):
    token = create_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk)).encode().decode()
    check_cache = cache.get(uid)
    if not check_cache:
        cache.set(uid, token, timeout=EXPIRE_MAIL)
        message = render_to_string('registration/user_activate_email.html', {
            'domain': domain,
            'uid': uid,
            'token': token
        })
        email = EmailMessage(EMAIL_TITLE, message, to=['l4538@naver.com'])
        email.send()
        return True
    else:
        False


def create_token(user):
    encoded = jwt.encode({'name': user.name,
                          'email': user.email,
                          'iat': timezone.now()
                          }, KEY, algorithm='HS256').decode()
    return encoded
