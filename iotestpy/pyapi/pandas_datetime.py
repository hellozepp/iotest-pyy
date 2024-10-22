from datetime import datetime

import pandas as pd
from pandas import Series
from pandas.api.types import is_datetime64_any_dtype as is_datetime


def ensure_datetime(series: Series, timezone: str):
    """
    Ensures that the `series` is a datetime series of dtype datetime64[ns, timezone]

    - Convert tz aware values to `timezone`.
    - Assume naive values are on `timezone` and make them aware.
    - Handle None values and convert them to NaT (so we can accomplish the dtype requirement).
    """
    if series.dtype == pd.DatetimeTZDtype(tz=timezone):
        return series

    are_datetime = series.apply(lambda x: isinstance(x, datetime)).astype(bool)

    # Convert only values that are not already datetime, otherwise if there are
    # tz-aware values pandas will raise: Tz-aware datetime.datetime cannot
    # be converted to datetime64 unless utc=True.
    # We cannot set utc=True because pandas will assume naive values to be on UTC
    # but we need naive values to be considered on `timezone`.
    series = series.mask(
        ~are_datetime, pd.to_datetime(series[~are_datetime], errors="coerce")
    )

    # Localize naive values to `timezone`
    are_unaware = series.apply(lambda x: not pd.isna(x) and x.tzinfo is None).astype(
        bool
    )
    series = series.mask(
        are_unaware, pd.to_datetime(series[are_unaware]).dt.tz_localize(timezone)
    )

    # Now that we don't have any naive value we can normalize all to UTC and
    # then convert to `timezone`.
    series = pd.to_datetime(series, utc=True).dt.tz_convert(timezone)

    return series


def test_ensure_datetime():
    series = pd.Series(
        ["2022-12-31 16:00:00-08:00", "2023-01-01", "2023-01-01 12:30", None]
    )

    series = ensure_datetime(series, "America/New_York")

    assert is_datetime(series)
    assert list(series) == [
        pd.Timestamp("2022-12-31 19:00", tz="America/New_York"),
        pd.Timestamp("2023-01-01 00:00", tz="America/New_York"),
        pd.Timestamp("2023-01-01 12:30", tz="America/New_York"),
        pd.NaT,
    ]

    series = ensure_datetime(series.dt.date, "America/New_York")

    assert is_datetime(series)
    assert list(series) == [
        pd.Timestamp("2022-12-31 00:00", tz="America/New_York"),
        pd.Timestamp("2023-01-01 00:00", tz="America/New_York"),
        pd.Timestamp("2023-01-01 00:00", tz="America/New_York"),
        pd.NaT,
    ]

    # Mix aware timestamps with naive
    series = pd.Series(
        [
            pd.Timestamp("2022-12-31 12:00", tz="America/New_York"),
            pd.Timestamp("2022-12-31 12:00"),
        ]
    )
    series = ensure_datetime(series, "America/New_York")
    assert list(series) == [
        pd.Timestamp("2022-12-31 12:00", tz="America/New_York"),
        pd.Timestamp("2022-12-31 12:00", tz="America/New_York"),
    ]
