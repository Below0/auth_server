import hashlib


def encrypt(pw):
    encoded_pw = pw.encode()
    return hashlib.sha256(encoded_pw).hexdigest()


def to_dict(name, email, pw):
    user_dict = {
        'name': name,
        'email': email,
        'pw': pw
    }
    return user_dict


