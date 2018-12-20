# coding=utf-8
print("#====================1==================")
import re

# patern = re.compile('www\..*', re.S)  # （re.S模式，“.”可以匹配“\n”
patern = re.compile('www\..*')
match1 = patern.match("www.baidu.comwww.baidu.com \nwww.baidu.com")
if match1:
    print(match1.group())
else:
    print("match1 don't match")
#    www.baidu.com
print("#====================2==================")
patern = re.compile('www\..*?')
match1 = patern.match("www.baidu.com")
if match1:
    print(match1.group())
else:
    print("match1 don't match")
# www.
print("#====================3==================")
tag = re.search(u'<mail-to>(?P<mail_name>.+?)</mail-to>?', "<mail-to>zhanglin04@daojia-inc.com</mail-to>")
if tag:
    print(tag.group('mail_name'))
