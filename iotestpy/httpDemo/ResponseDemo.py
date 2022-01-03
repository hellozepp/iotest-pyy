# -*- coding:utf-8 -*-
import requests

url = 'https://www.csdn.net/'
r = requests.get(url, timeout=20)
if r.status_code == requests.codes.ok:
    print('=== status_code === ', r.status_code)  # 响应码
    print('=== headers === ', r.headers)  # 响应头
    print('=== Content-Type === ', r.headers.get('Content-Type'))  # 获取响应头中的Content-Type字段
else:
    r.raise_for_status()  # 抛出异常
