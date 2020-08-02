import os
import json
import struct

def upload():

    # 得到用户要上传的文件描述信息
    dir_path = input("file_path:")
    file_name = input("file_name:")
    file_complete_path = os.path.join(dir_path,file_name)
    file_size = os.path.getsize(file_complete_path)
    file_info = {
        "dir_path":dir_path,
        "file_name":file_name,
        "complete_path":file_complete_path,
        "file_size":file_size
    }

    # 将文件描述信息封装成报头
    file_info_json = json.dumps(file_info)
    send_len_to_server = struct.pack("i",len(file_info_json))

    # 将报头的长度发送到服务端
    #


    # 将报头发送到服务端
    # send(file_info_json)


    # 开始读取文件信息, 并上传
    size = 0
    with open(file_info["complete_path"],'rb') as f:
        while size<file_size:
            data = f.read(1024)
            # 发送数据到服务端
            #
            size += len(data)


def download():
    # 接收服务端给的所有文件名
    # recv()
    # 根据编号, 选择相对应的文件, 得到该文件名
    # 下载该文件
    pass