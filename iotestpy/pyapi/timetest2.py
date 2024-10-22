import datetime
from typing import Optional

import pytz
import sys
from zoneinfo import ZoneInfo

print("===================pytz=====================")
# pytz需要安装，但在python3.9中不推荐，因为已经内置了zoneinfo
tz = pytz.timezone("UTC")
timestamp = 1725505678  # 2024-09-05 11:07:58 +08:00
d = datetime.datetime.fromtimestamp(timestamp, tz=pytz.UTC)

# 打印原始 UTC 时间
print("Original UTC time:", d)

# 定义上海时区
tz_shanghai = pytz.timezone("Asia/Shanghai")

# 将 UTC 时间转换为上海时间
d_shanghai = d.astimezone(tz_shanghai)

# 打印转换后的上海时间
print("Converted Shanghai time:", d_shanghai)

# 检查是否受夏令时影响
print("Is DST:", bool(d_shanghai.dst()))
print("Converted Shanghai time:", tz.normalize(d_shanghai))

print("==========py39===========")

# 定义 UTC 时区
tz_utc = ZoneInfo("UTC")

# 创建一个 UTC 时区的 datetime 对象
d = datetime.datetime(1986, 5, 4, 0, 30, 0, 78, tzinfo=tz_utc)

# 打印原始 UTC 时间
print("Original UTC time:", d)

# 定义上海时区
tz_shanghai = ZoneInfo("Asia/Shanghai")

# 将 UTC 时间转换为上海时间
d_shanghai = d.astimezone(tz_shanghai)

# 打印转换后的上海时间
print("Converted Shanghai time:", d_shanghai)

# datetime 的  dt.replace(tzinfo=timezone) 方法不会转换时区，只是修改时区信息，因此需要使用 astimezone() 方法来转换时区。
print("replace to africa/johannesburg:", d_shanghai.replace(tzinfo=pytz.timezone("Africa/Johannesburg")))

print("=====================")
d = datetime.datetime(year=1986, month=5, day=4, hour=0, minute=30, second=0,
                      microsecond=78, tzinfo=tz)
print("年：{} 月：{} 日：{} 时：{} 分：{} 秒：{} 亚秒：{} 时区：{}".format(d.year, d.month, d.day, d.hour, d.minute, d.second,
                                                                   d.microsecond, d.tzinfo))
d = datetime.datetime(year=1986, month=5, day=4, hour=0, minute=30, second=0,
                      microsecond=78)
# 不新建一个没tz的dt的话，ValueError: Not naive datetime (tzinfo is already set)
d = pytz.UTC.localize(d, is_dst=None)
print("年：{} 月：{} 日：{} 时：{} 分：{} 秒：{} 亚秒：{} 时区：{}".format(d.year, d.month, d.day, d.hour, d.minute, d.second,
                                                                   d.microsecond, d.tzinfo))
d = datetime.datetime(year=1986, month=5, day=4, hour=0, minute=30, second=0,
                      microsecond=78)
d = pytz.UTC.localize(d, is_dst=None)
print("年：{} 月：{} 日：{} 时：{} 分：{} 秒：{} 亚秒：{} 时区：{}".format(d.year, d.month, d.day, d.hour, d.minute, d.second,
                                                                   d.microsecond, d.tzinfo))

d = tz.normalize(d)  # 用来修正神奇的没听说过的夏令时，会转成本地时区
# UTC 中没有夏令时，因此它是执行日期算术的有用时区，而无需担心夏令时转换、您所在国家/地区更改其时区或在多个时区漫游的移动计算机造成的混乱和歧义。

print("年：{} 月：{} 日：{} 时：{} 分：{} 秒：{} 亚秒：{} 时区：{}".format(d.year, d.month, d.day, d.hour, d.minute, d.second,
                                                                   d.microsecond, d.tzinfo))
print("===========================================================")

from datetime import datetime

print(datetime.today())
print(datetime.now())
print(datetime.now().strftime('%Y-%m-%d %H-%M-%S'))

print("===========================================================")

import time

s = datetime(2012, 6, 22, 5, 5, 5)
print(time.mktime(s.timetuple()))

timeTuple = time.localtime(1340312705.0)
print(time.strftime('%Y-%m-%d %H-%M-%S', timeTuple))

print("===============================使用zoneinfo start from python3.9============================")
# pip install tzdata
# 超过3.9也可以安装，会提示Requirement already satisfied: tzdata in ./.venv/lib/python3.9/site-packages (2024.1)
from zoneinfo import ZoneInfo
from datetime import datetime, timezone

# from zoneinfo import ZoneInfo
print("As you can see there is a 2hr diff between Africa/Johannesburg and UTC")
my_datetime = datetime(2021, 10, 31, 0, 0, tzinfo=ZoneInfo('Africa/Johannesburg'))
print(my_datetime.astimezone(timezone.utc))
print(datetime(2021, 10, 30, 22, 0, tzinfo=timezone.utc))

# 等价 pytz的 LTZ
# pytz.UTC.localize(my_datetime, is_dst=None)
# 如果不带参数调用（或tz=None），则假定系统本地时区。转换后的datetime实例的.tzinfo属性将被设置为一个timezone实例，该实例具有从操作系统获得的区域名称和偏移量。
print(datetime(2020, 6, 11, 12, tzinfo=None).astimezone())

today = datetime.now(ZoneInfo("America/Los_Angeles"))

print(today)

print(today.tzinfo)

print("===========================pytz================================")
import datetime

PY39 = sys.version_info >= (3, 9)
if PY39:
    from zoneinfo import ZoneInfo
else:
    import pytz
    from dateutil import tz

def as_timezone(dt: datetime.datetime, timezone_str: Optional[str],
                is_timestamp_ntz: bool = False) -> datetime.datetime:
    if PY39:
        from zoneinfo import ZoneInfo
        if is_timestamp_ntz:
            timezone = ZoneInfo("UTC")
        elif timezone_str:
            timezone = ZoneInfo(timezone_str)
        else:
            # System default timezone
            timezone = None
    else:
        from dateutil import tz
        if is_timestamp_ntz:
            timezone = tz.tzutc()
        elif timezone_str:
            timezone = tz.gettz(timezone_str)
        else:
            timezone = tz.tzlocal()

    return dt.astimezone(timezone)
print("===========================tzlocal================================")
import tzlocal
lz = tzlocal.get_localzone()
# zoneinfo.ZoneInfo(key='Asia/Shanghai')
# tzlocal version should >= 5.0.0
print(lz.key)
