import string
from django.utils.baseconv import base64
import json
import socket
EXPIRE_HOUR = 60 * 60
EXPIRE_DAY = 24 * EXPIRE_HOUR
EXPIRE_WEEK = EXPIRE_DAY * 7
EXPIRE_MAIL = 180

KEY = 'DevCamp'

EMAIL_TITLE = '계정 생성 인증메일입니다.'
EMAIL_CONTENT = '계정 인증 링크 : '

