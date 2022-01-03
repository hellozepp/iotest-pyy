# -*- coding:utf-8 -*-
import json
from urllib.parse import quote

import requests

url = 'http://127.0.0.1:12345/api_v1/writelog'
data = quote(json.dumps(
    {"sendLog": {"token": "=zhanglin&x", "logLine": "xxx"}}, ensure_ascii=False))

headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
requests = requests.post(url, data=data, headers=headers)
print(requests.content)
