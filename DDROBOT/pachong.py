# coding:utf-8

import os
import uuid

import requests


def pc(dz, uil):
    uuid_str = uuid.uuid4().hex
    tmp_file_name = 'tmpfile_%s.png' % uuid_str
    print(tmp_file_name)
    url = uil  # 图片地址
    root = fr"{dz}"  # 存放图片路径
    path = root + 'DD'+tmp_file_name   # 设置图片名称及其格式
    try:  # try···except结构，返回链接错误类型
        headers = {'user-agent': 'Mozilla/5.0'}  # 请求头模拟
        # 使用库os的方法确认文件路径是否存在，若不存在则创建
        if not os.path.exists(root):
            os.mkdir(root)  # 若不存在则创建
        if not os.path.exists(path):
            r = requests.get(url, headers=headers)
            with open(path, 'wb') as f:  # "wb'表示对二进制文件的写入
                f.write(r.content)  # r.content表示返回内容的二进制形式
                f.close()  # with··· as 语句会自动关闭句柄，可不写close()
                print("文件保存成功", root)

        else:
            print('文件已经存在')

    except ConnectionError as err:
        print(err)
while True:
    pc('E:/pic/', 'https://api.iyk0.com/mtt')
