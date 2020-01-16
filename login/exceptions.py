class AuthFailureException(Exception):
    def __init__(self):
        super().__init__('로그인에 실패하였습니다.')