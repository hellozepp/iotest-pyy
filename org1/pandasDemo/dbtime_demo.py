# Using the db-dtypes package

import datetime
import re
from typing import Optional

import pandas as pd
import db_dtypes  # noqa import to register dtypes
import pytest
from dateutil import relativedelta
from pandas import Timedelta

# 导入db_dtypes模块会注册扩展dtypes以在pandas中使用。
# 使用 YYYY-MM-DD 格式的字符串或 datetime.date 对象构造日期 Series 。
dates = pd.Series([datetime.date(2021, 9, 17), "2021-9-18"], dtype="dbdate")
print("dates: ", dates)
# Working with dates¶
# Convert a date Series to a datetime64 Series with astype().
datetimes = dates.astype("datetime64")
print("datetimes: ", datetimes)

# 像datetime 64值一样，日期值可以被减去。这相当于先转换为datetime 64，然后再减去。
dates2 = pd.Series(["2021-1-1", "2021-1-2"], dtype="dbdate")
diffs = dates - dates2
print("diffs: ", diffs)
# ie: numpy.timedelta64
print("time delta: ", Timedelta("259 days 00:00:00"))

# 像datetime 64值一样，DateOffset值可以添加到它们中。
do = pd.DateOffset(days=1)
after = dates + do
before = dates - do
print("after: ", after)
print("before: ", before)

# Working with times
times = pd.Series([datetime.time(1, 2, 3, 456789), "12:00:00.6"], dtype="dbtime")
# Convert a time Series to a timedelta64 Series with astype().
timedeltas = times.astype("timedelta64")
print("timedeltas: ", timedeltas)
# ie: numpy.timedelta64
print("numpy Timedelta: ", Timedelta("0 days 01:02:03.456789"))
# Combining dates and times¶
combined = dates + times
print("combined: ", combined)

# relativedelta相比于DateOffset和timedelta确实有一些优势:
#
# 对比DateOffset:
#
# relativedelta更灵活,可以同时处理年、月、日、小时等多个时间单位。
# 它可以更方便地处理月末问题,比如在1月31日加一个月。
# relativedelta支持更复杂的日期运算,如"下一个工作日"。
#
#
# 对比timedelta:
#
# relativedelta可以处理年和月,而timedelta只能处理天及更小的单位。
# 使用relativedelta进行日期计算时,会自动处理闰年等情况。

# relativedelta
# BigQuery sends INTERVAL data in "canonical format"
# https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#interval_type
_INTERVAL_PATTERN = re.compile(
    r"(?P<calendar_sign>-?)(?P<years>\d+)-(?P<months>\d+) "
    r"(?P<days>-?\d+) "
    r"(?P<time_sign>-?)(?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+)\.?(?P<fraction>\d*)?$"
)

def _interval_from_json(
    value: Optional[str]
) -> Optional[relativedelta.relativedelta]:
    """Coerce 'value' to an interval, if set or not nullable."""
    if not value:
        return None

    parsed = _INTERVAL_PATTERN.match(value)
    if parsed is None:
        raise ValueError(f"got interval: '{value}' with unexpected format")

    calendar_sign = -1 if parsed.group("calendar_sign") == "-" else 1
    years = calendar_sign * int(parsed.group("years"))
    months = calendar_sign * int(parsed.group("months"))
    days = int(parsed.group("days"))
    time_sign = -1 if parsed.group("time_sign") == "-" else 1
    hours = time_sign * int(parsed.group("hours"))
    minutes = time_sign * int(parsed.group("minutes"))
    seconds = time_sign * int(parsed.group("seconds"))
    fraction = parsed.group("fraction")
    microseconds = time_sign * int(fraction.ljust(6, "0")[:6]) if fraction else 0

    return relativedelta.relativedelta(
        years=years,
        months=months,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        microseconds=microseconds,
    )



@pytest.mark.parametrize(
    ("value", "expected"),
    (
        ("0-0 0 0:0:0", relativedelta.relativedelta()),
        # SELECT INTERVAL X YEAR
        ("-10000-0 0 0:0:0", relativedelta.relativedelta(years=-10000)),
        ("-1-0 0 0:0:0", relativedelta.relativedelta(years=-1)),
        ("1-0 0 0:0:0", relativedelta.relativedelta(years=1)),
        ("10000-0 0 0:0:0", relativedelta.relativedelta(years=10000)),
        # SELECT INTERVAL X MONTH
        ("-0-11 0 0:0:0", relativedelta.relativedelta(months=-11)),
        ("-0-1 0 0:0:0", relativedelta.relativedelta(months=-1)),
        ("0-1 0 0:0:0", relativedelta.relativedelta(months=1)),
        ("0-11 0 0:0:0", relativedelta.relativedelta(months=11)),
        # SELECT INTERVAL X DAY
        ("0-0 -3660000 0:0:0", relativedelta.relativedelta(days=-3660000)),
        ("0-0 -1 0:0:0", relativedelta.relativedelta(days=-1)),
        ("0-0 1 0:0:0", relativedelta.relativedelta(days=1)),
        ("0-0 3660000 0:0:0", relativedelta.relativedelta(days=3660000)),
        # SELECT INTERVAL X HOUR
        ("0-0 0 -87840000:0:0", relativedelta.relativedelta(hours=-87840000)),
        ("0-0 0 -1:0:0", relativedelta.relativedelta(hours=-1)),
        ("0-0 0 1:0:0", relativedelta.relativedelta(hours=1)),
        ("0-0 0 87840000:0:0", relativedelta.relativedelta(hours=87840000)),
        # SELECT INTERVAL X MINUTE
        ("0-0 0 -0:59:0", relativedelta.relativedelta(minutes=-59)),
        ("0-0 0 -0:1:0", relativedelta.relativedelta(minutes=-1)),
        ("0-0 0 0:1:0", relativedelta.relativedelta(minutes=1)),
        ("0-0 0 0:59:0", relativedelta.relativedelta(minutes=59)),
        # SELECT INTERVAL X SECOND
        ("0-0 0 -0:0:59", relativedelta.relativedelta(seconds=-59)),
        ("0-0 0 -0:0:1", relativedelta.relativedelta(seconds=-1)),
        ("0-0 0 0:0:1", relativedelta.relativedelta(seconds=1)),
        ("0-0 0 0:0:59", relativedelta.relativedelta(seconds=59)),
        # SELECT (INTERVAL -1 SECOND) / 1000000
        ("0-0 0 -0:0:0.000001", relativedelta.relativedelta(microseconds=-1)),
        ("0-0 0 -0:0:59.999999", relativedelta.relativedelta(seconds=-59, microseconds=-999999)),
        ("0-0 0 -0:0:59.999", relativedelta.relativedelta(seconds=-59, microseconds=-999000)),
        ("0-0 0 0:0:59.999", relativedelta.relativedelta(seconds=59, microseconds=999000)),
        ("0-0 0 0:0:59.999999", relativedelta.relativedelta(seconds=59, microseconds=999999)),
        # Test with multiple digits in each section.
        (
            "32-11 45 67:16:23.987654",
            relativedelta.relativedelta(
                years=32,
                months=11,
                days=45,
                hours=67,
                minutes=16,
                seconds=23,
                microseconds=987654,
            ),
        ),
        (
            "-32-11 -45 -67:16:23.987654",
            relativedelta.relativedelta(
                years=-32,
                months=-11,
                days=-45,
                hours=-67,
                minutes=-16,
                seconds=-23,
                microseconds=-987654,
            ),
        ),
        # Test with mixed +/- sections.
        (
            "9999-9 -999999 9999999:59:59.999999",
            relativedelta.relativedelta(
                years=9999,
                months=9,
                days=-999999,
                hours=9999999,
                minutes=59,
                seconds=59,
                microseconds=999999,
            ),
        ),
        # Test with fraction that is not microseconds.
        ("0-0 0 0:0:42.", relativedelta.relativedelta(seconds=42)),
        ("0-0 0 0:0:59.1", relativedelta.relativedelta(seconds=59, microseconds=100000)),
        ("0-0 0 0:0:0.12", relativedelta.relativedelta(microseconds=120000)),
        ("0-0 0 0:0:0.123", relativedelta.relativedelta(microseconds=123000)),
        ("0-0 0 0:0:0.1234", relativedelta.relativedelta(microseconds=123400)),
        # Fractional seconds can cause rounding problems if cast to float. See:
        # https://github.com/googleapis/python-db-dtypes-pandas/issues/18
        ("0-0 0 0:0:59.876543", relativedelta.relativedelta(seconds=59, microseconds=876543)),
        (
            "0-0 0 01:01:01.010101",
            relativedelta.relativedelta(hours=1, minutes=1, seconds=1, microseconds=10101),
        ),
        (
            "0-0 0 09:09:09.090909",
            relativedelta.relativedelta(hours=9, minutes=9, seconds=9, microseconds=90909),
        ),
        (
            "0-0 0 11:11:11.111111",
            relativedelta.relativedelta(hours=11, minutes=11, seconds=11, microseconds=111111),
        ),
        (
            "0-0 0 19:16:23.987654",
            relativedelta.relativedelta(hours=19, minutes=16, seconds=23, microseconds=987654),
        ),
        # Nanoseconds are not expected, but should not cause error.
        ("0-0 0 0:0:00.123456789", relativedelta.relativedelta(microseconds=123456)),
        ("0-0 0 0:0:59.87654321", relativedelta.relativedelta(seconds=59, microseconds=876543)),
    ),
)
def test_w_string_values(value, expected):
    got = _interval_from_json(value)
    assert got == expected