import socket
import hashlib

secret_key = b'zxj'
hslb = hashlib.md5(secret_key)



sk = socket.socket()
sk.connect(('127.0.0.1',8080))
legal = sk.recv(1024)
hslb.update(legal)
is_legal = hslb.hexdigest()
sk.send(is_legal.encode())
hefa = sk.recv(1024).decode()
if hefa:
    while True:
        uin = input(">>>")
        if uin == 'q':
            break
        sk.send(uin.encode())
else:
    print("非法客户端")
sk.close()
