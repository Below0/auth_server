class AuthFailureException(Exception):
    def __init__(self):
        super().__init__('로그인에 실패하였습니다.')


class NotEmailAuthException(Exception):
    def __init__(self):
        super().__init__('이메일 인증이 필요합니다.')
