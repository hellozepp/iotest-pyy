import datetime
import sys
import unittest
from typing import Optional
from unittest.mock import patch

PY39 = sys.version_info >= (3, 9)
from dateutil import tz

if PY39:
    from zoneinfo import ZoneInfo


def as_timezone(dt: datetime.datetime, timezone_str: Optional[str],
                is_timestamp_ntz: bool = False) -> datetime.datetime:
    if PY39:
        if is_timestamp_ntz:
            return dt.replace(tzinfo=ZoneInfo("UTC"))
        if not dt.tzinfo:
            dt = dt.replace(tzinfo=ZoneInfo("UTC"))
        if timezone_str:
            timezone = ZoneInfo(timezone_str)
        else:
            # System default timezone
            timezone = None
    else:
        if is_timestamp_ntz:
            return dt.replace(tzinfo=tz.tzutc())
        if not dt.tzinfo:
            dt = dt.replace(tzinfo=tz.tzutc())
        if timezone_str:
            timezone = tz.gettz(timezone_str)
        else:
            timezone = tz.tzlocal()

    return dt.astimezone(timezone)


class TestReplaceDatetimeTimezone(unittest.TestCase):

    @patch('iotestpy.pyapi.PY39', new=True)
    def test_replace_datetime_timezone_py39(self):
        from zoneinfo import ZoneInfo

        dt = datetime.datetime(2024, 9, 5, 3, 7, 58)
        dt = as_timezone(dt, "America/New_York")
        self.assertEqual(dt.tzinfo, ZoneInfo("America/New_York"))

        dt = datetime.datetime(2024, 9, 5, 3, 7, 58, tzinfo=ZoneInfo("America/New_York"))
        dt = as_timezone(dt, None, is_timestamp_ntz=True)
        self.assertEqual(dt.tzinfo, ZoneInfo("UTC"))

        # Test America/New_York timezone replace to local timezone
        tzinfo = datetime.datetime(2024, 9, 5, 3, 7, 58, tzinfo=None).astimezone().tzinfo
        dt = datetime.datetime(2024, 9, 5, 3, 7, 58, tzinfo=ZoneInfo("America/New_York"))
        dt = as_timezone(dt, None, False)
        self.assertEqual(dt.tzinfo, tzinfo)

    @patch('iotestpy.pyapi.PY39', new=False)
    def test_replace_datetime_timezone_pre_py39(self):
        from dateutil import tz
        dt = datetime.datetime(2024, 9, 5, 3, 7, 58)
        dt = as_timezone(dt, "America/New_York")
        self.assertTrue("America/New_York" in dt.tzinfo._filename)

        # There is a 2hr diff between Africa/Johannesburg and UTC
        excepted = datetime.datetime(2021, 10, 30, 22, 0, tzinfo=tz.tzutc())
        dt = datetime.datetime(2021, 10, 31, 0, 0, tzinfo=tz.gettz('Africa/Johannesburg'))
        dt = as_timezone(dt, "UTC")
        self.assertTrue("UTC" in dt.tzinfo._filename)
        self.assertEqual(dt, excepted)

        dt = datetime.datetime(2024, 9, 5, 3, 7, 58)
        dt = as_timezone(dt, None, is_timestamp_ntz=True)
        self.assertEqual(dt.tzinfo, tz.tzutc())

        # Test local timezone
        dt = datetime.datetime(2024, 9, 5, 3, 7, 58, tzinfo=tz.gettz("America/New_York"))
        dt = as_timezone(dt, None, is_timestamp_ntz=False)
        # Check if the timezone is the same as the local timezone
        self.assertEqual(dt.tzinfo, tz.tzlocal())
