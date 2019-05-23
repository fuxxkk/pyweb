import hashlib
import time


def md5_encode(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


def create_uuid():
    return md5_encode(str(time.clock()))
