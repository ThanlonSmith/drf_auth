import hashlib, time


def md5(name):
    obj = hashlib.md5(bytes(name, encoding='utf-8'))
    ctime = str(time.time())
    obj.update(bytes(ctime, encoding='utf-8'))
    return obj.hexdigest()
