import socket
import json
class MySocketClient:
    def __init__(self):
        self.sk = socket.socket()
        self.sk.connect(('127.0.0.1',8080))


    def send_verify_msg(self,msg):
        msg = json.dumps(msg).encode()
        self.sk.send(msg)