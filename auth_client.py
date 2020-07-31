import hashlib

# 验证合法性
def verify(ser_ver):
    secret_key = b'zxj'
    hslb = hashlib.md5(secret_key)
    hslb.update(ser_ver)
    code = hslb.hexdigest()
    return code