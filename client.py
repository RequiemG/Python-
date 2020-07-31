import socket
import hashlib
import auth_client
import json

sk = socket.socket()
sk.connect(('127.0.0.1',8080))

# 验证合法性
legal_code = sk.recv(1024)
auth_code = auth_client.verify(legal_code)
sk.send(auth_code.encode())
is_hefa = sk.recv(1024).decode()


# 判断是否合法
if is_hefa:

    # 合法的, 让用户输入账号密码
    while True:
        acc = input("acc:")
        pwd = input("pwd:")
        user_info = {"account":acc,"password":pwd}
        user_info_json_bytes = json.dumps(user_info).encode()
        sk.send(user_info_json_bytes)

        is_true = sk.recv(1024).decode()
        print(is_true)


        if is_true == "登入成功":
            print(is_true)
            break
        else:
            print("登入是包")


    while True:
        uin = input(">>>")
        if uin == 'q':
            break
        sk.send(uin.encode())
else:
    print("非法客户端")
sk.close()
