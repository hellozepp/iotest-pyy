# -*- coding:utf-8 -*-
import requests

# 以下为GET请求
url = 'https://www.csdn.net/'
requests = requests.get(url)
print(requests.content)  # 返回字节形式
