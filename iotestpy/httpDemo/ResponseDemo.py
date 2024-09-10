# -*- coding:utf-8 -*-
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

retries = Retry(
    total=5,  # 总重试次数
    backoff_factor=1,  # 指数退避因子
    status_forcelist=[500, 502, 503, 504],  # 指定哪些状态码触发重试
    allowed_methods=frozenset(['GET', 'POST']),  # 允许重试的HTTP方法
)
session = requests.Session()
adapter = HTTPAdapter(max_retries=retries)

session.mount('http://', adapter)
session.mount('https://', adapter)

url = 'https://www.csdn.net/'
r = session.get(url, timeout=20)
if r.status_code == requests.codes.ok:
    print('=== status_code === ', r.status_code)  # 响应码
    print('=== headers === ', r.headers)  # 响应头
    print('=== Content-Type === ', r.headers.get('Content-Type'))  # 获取响应头中的Content-Type字段
else:
    r.raise_for_status()  # 抛出异常
