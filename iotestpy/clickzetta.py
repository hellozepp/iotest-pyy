# 会导致循环引用，因为clickzetta.py的module name和要import的module name相同，所以会导致循环引用
# ImportError: cannot import name 'connect' from partially initialized module 'clickzetta' (most likely due to a circular import) (/Users/zhanglin/PycharmProjects/iotest-pyy/iotestpy/clickzetta.py)
from clickzetta import connect
print("ok")