import random
import hashlib

import jwt
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.cache import cache
from .exceptions import *
from django.core.mail import EmailMessage
from .constants import *


def encrypt(pw):
    encoded_pw = pw.encode()
    return hashlib.sha256(encoded_pw).hexdigest()


def create_salt():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(8))


def is_valid_token(token):
    check_token = cache.get(token)
    if check_token:
        return check_token
    else:
        return None



