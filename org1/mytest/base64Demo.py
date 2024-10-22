import base64
import gzip

s = """
set cz.sql.string.literal.escape.mode=QUOTE;
select 'a''b';
"""

# 对字符串进行gzip压缩，然后进行base64编码；为什么要b64encode然后decode呢？ 因为b64encode返回的是bytes类型，而我们需要的是str类型
b = base64.b64encode(gzip.compress(s.encode())).decode()
print("b64encode:", b)
# 对base64解码，然后进行gzip解压缩
c = gzip.decompress(base64.b64decode(b)).decode()
print("b64decode:", c)
