from core.Socket_Client import MySocketClient

class Auth_client:

    def __init__(self):
        self.sk = MySocketClient()

    def login(self):
        username = input("username:")
        password = input("password:")
        if username.strip() and password.strip():
            # 得到用户名密码,组成字典
            verify_msg = {"username":username,"password":password}
            # 把该账户信息字典发送给服务端
            MySocketClient.send_verify_msg(verify_msg)
            # 服务器返回验证信息
        server_veri_info = self.sk.recv(1024)


    def register(self):
        username = input("username:")
        password1 = input("password:")
        password2 = input("password_ensure:")
        if username.strip() and password.strip() and password1==password2:
            verify_msg = {"username":username,"password":password}
            MySocketClient.send_verify_msg(verify_msg)
