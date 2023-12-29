import sys
import uuid
import requests
import base64
import hashlib
import os
import ast
import binascii

from imp import reload


class Translate():
    reload(sys)
    YOUDAO_URL = "https://openapi.youdao.com/ocrtransapi"
    APP_KEY = '7e782f78aec29bd2'
    APP_SECRET = 'Qrp2mhpcsmYpG0KWHGAgI8rIWuzuA2FV'

    def truncate(q):
        if q is None:
            return None
        size = len(q)
        if size <= 20:
            return q
        else:
            # 取前10个，总长度，后10个
            return q[0:10] + str(size) + q[size - 10:size]

    # 摘要算法
    def encrypt(signStr):
        hash_algorithm = hashlib.md5()
        # encode将signStr处理为二进制格式
        hash_algorithm.update(signStr.encode("utf-8"))
        # 获取哈希加密后的16进制字符串
        return hash_algorithm.hexdigest()

    def do_request(data):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        return requests.post(Translate.YOUDAO_URL, data=data, headers=headers)

    # 转换算法，从16进制字符串utf-8变化为汉字
    def utfTrans(string):
        temp1 = string.encode("unicode_escape")
        temp2 = temp1.decode("utf-8").replace("\\x", '')
        result = binascii.a2b_hex(temp2).decode("utf-8")
        return result

    # 转换算法，将互联网2进制字典变为普通字典
    def dictTrans(binary_dict):
        # 转化为字符串形式的字典
        temp = binary_dict.decode("utf-8")
        return ast.literal_eval(temp)

    # 根据网页返回结果，将识别出的原文与译文写入文本文档
    def write_in_text(file_address, photo_address, binary_download_dict):
        # 从网上获得的字典是二进制的，需要转化
        dict = Translate.dictTrans(binary_download_dict)
        # 获取没有扩展名的图片文件名
        photo_name = os.path.basename(photo_address)
        pre, back = os.path.splitext(photo_name)
        # 进入指定的需要创建新文件的文件夹
        os.chdir(file_address)
        # 写模式新建文件，如果已存在则报错
        with open(pre + '.txt', 'w+', encoding="utf-8") as f:
            for resRegion in dict["resRegions"]:
                context = resRegion["context"]
                f.write("原文：" + context + "\n")
                tranContent = resRegion["tranContent"]
                f.write("译文：" + tranContent + "\n")
                f.write("\n")
        f.close()

    def connect(self, file_address, photo_address):
        # 以二进制方式打开图片
        f = open(photo_address, "rb")
        # 读取文件内容并转换为base64编码
        q = base64.b64encode(f.read()).decode("utf-8")
        f.close()

        data = {}
        data["from"] = "auto"
        data["to"] = "auto"
        data["type"] = "1"
        data["q"] = q
        salt = str(uuid.uuid1())
        signStr = Translate.APP_KEY + q + salt + Translate.APP_SECRET
        sign = Translate.encrypt(signStr)
        data["appKey"] = Translate.APP_KEY
        data["salt"] = salt
        data["sign"] = sign

        response = Translate.do_request(data)
        Translate.write_in_text(file_address, photo_address, response.content)
