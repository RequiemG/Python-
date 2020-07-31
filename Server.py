import socketserver
import hashlib
import os
import json
import auth_client



rand = os.urandom(3)
verify_code = auth_client.verify(rand)


class MySocketServer(socketserver.BaseRequestHandler):

    # 验证客户端是否合法
    def setup(self):
        self.request.send(rand)
        ret = self.request.recv(1024).decode()
        if verify_code == ret:
            print("客户端合法")
            self.request.send("Authentication is successful".encode())
        else:
            print("非法客户端")
            self.request.send("".encode())
            self.request.close()
        while True:
            user_info = json.loads(self.request.recv(1024).decode())
            if user_info["account"] == 'zxj' and user_info["password"] == 'qwer':
                self.request.send("登入成功".encode())
                print(f"用户{self.client_address}{user_info['account']}登入")
                break
            else:
                self.request.send("用户名或密码错误".encode())


    # 对合法的用户端进行用户认证
    def handle(self):

        pass

    # 上传下载文件
    def finish(self):
        try:
            while True:
                ret = self.request.recv(1024).decode()
                if len(ret) == 0:
                    print(f"{self.client_address}正常退出.........")
                    break
                print(f"来自{self.client_address}:的信息:{ret}")
        except ConnectionResetError:
            print(f"{self.client_address}断开连接")


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8080),MySocketServer)
    server.serve_forever()