import re
from xml import etree

import requests
from requests.adapters import HTTPAdapter

class GetResponse(object):
    def __init__(self):
        self.session = requests.Session()
        self.session.keep_alive = False
        self.session.mount('http://', HTTPAdapter(max_retries=3))
        self.session.mount('https://', HTTPAdapter(max_retries=3))

    def getResp(self, url, headers=None, res=None):
        try:
            res = self.session.get(url, headers=headers, timeout=20,
                                   proxies=self.proxys,
                                   allow_redirects=False, verify=False)
            if res.encoding == "GB2312":
                res.encoding = "gbk"
            else:
                try:
                    chareset = re.findall("charset=[\"|']{0,1}(.*?)\"", res.text)[0]
                    res.encoding = chareset.strip("'").strip('"').lower()
                except Exception:
                    res.encoding = "utf-8"
                if res.status_code != 200:
                    if res.status_code == 301 or res.status_code == 302:
                        res = self.session.get(url, headers=headers,
                                               proxies=self.proxys,
                                               timeout=20, verify=False)
                        try:
                            chareset = re.findall("charset=[\"|']{0,1}(.*?)\"", res.text)[0]
                            res.encoding = chareset.strip("'").strip('"').lower()
                        except Exception:
                            res.encoding = "utf-8"
            return res
        except Exception:
            return res

    def getHtml(self, url, headers=None, html=None):
        try:
            res = self.getResp(url, headers)
            if res is not None or res.status_code == 200:
                try:
                    html = etree.HTML(res.text)
                except Exception:
                    html = etree.HTML(res.content)
            return html
        except Exception:
            return html