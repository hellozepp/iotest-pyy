from enum import IntEnum, unique, Enum, auto


@unique
class Season(IntEnum):
    spring = 1
    summer = 2
    autumn = 3
    winter = 4
    # winter2=4 #使用了@unique 不允许重复


# print(Season())#enum不能定义对象
print(Season.spring)
print(Season(2))

print(Season.winter.value)
print(Season["autumn"].value)

for s in Season:
    print(s)

# =============================================================
print("==========================================")


class RetryStatus(Enum):
    """Retry status codes"""
    THROTTLED = auto() # 从 1 开始
    FAILED = auto()
    NOT_FOUND = auto()
    INTERNAL_ERROR = 10
    PRECHECK_FAILED = auto() # 从 11 继续
    STREAM_UNAVAILABLE = auto()

for s in RetryStatus:
    print(s.value)