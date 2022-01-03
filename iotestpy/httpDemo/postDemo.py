# -*- coding:utf-8 -*-
import json

import requests

# 以下为POST请求
url = 'http://127.0.0.1:64700/v2/writelog'
data = json.dumps(
    {"sendLog": {"token": "78fd4d1a-796a-48d3-bcb2-a5ec5f0fc00e", "logLine": "xxx"}}, ensure_ascii=False)

headers = {'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'}
requests = requests.post(url, data=data, headers=headers)
print(requests.content)  # 返回字节形式
