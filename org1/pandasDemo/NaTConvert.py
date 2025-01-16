import pandas as pd
import pyarrow as pa
from datetime import datetime

print("Does NaT is nan? ", pd.isna(pd.NaT)) # True
# 创建包含各种时间类型的测试数据
df = pd.DataFrame({
    'timestamp': [
        pd.Timestamp('2023-01-01'),
        pd.NaT,
        pd.Timestamp('2023-01-03'),
        None
    ],
    'datetime': [
        datetime(2023, 1, 1),
        pd.NaT,
        datetime(2023, 1, 3),
        None
    ],
    'date': [
        pd.Timestamp('2023-01-01').date(),
        pd.NaT,
        pd.Timestamp('2023-01-03').date(),
        None
    ],
    'values': [10, 20, 30, 40]
})

print("Original DataFrame:")
print(df)
print("\nDataFrame dtypes:")
print(df.dtypes)

print("方法1: 直接转换（让我们看看是否会报错）")
try:
    table1 = pa.Table.from_pandas(df)
    print("\nMethod 1 - Direct conversion successful:")
    print(table1)
except Exception as e:
    print("\nMethod 1 failed:", e)

# 方法2: 手动处理NaT
processed_data = {
    'timestamp': [
        None if pd.isna(val) or val is None else val
        for val in df['timestamp']
    ],
    'datetime': [
        None if pd.isna(val) or val is None else val
        for val in df['datetime']
    ],
    'date': [
        None if pd.isna(val) or val is None else val
        for val in df['date']
    ],
    'values': df['values']
}

# 创建Arrow数组
timestamp_array = pa.array(processed_data['timestamp'], type=pa.timestamp('us', tz='UTC'))
datetime_array = pa.array(processed_data['datetime'], type=pa.timestamp('us'))
date_array = pa.array(processed_data['date'], type=pa.date32())
values_array = pa.array(processed_data['values'])

# 创建Arrow表
table2 = pa.Table.from_arrays(
    arrays=[timestamp_array, datetime_array, date_array, values_array],
    names=['timestamp', 'datetime', 'date', 'values']
)

print("\nMethod 2 - Manual conversion result:")
print(table2)

# 验证NULL值
print("\nChecking null values in Arrow table:")
for column in table2.column_names:
    null_count = table2[column].null_count
    print(f"{column}: {null_count} null values")

# 转换回Pandas验证
df_back = table2.to_pandas()
print("\nConverted back to Pandas:")
print(df_back)
print("\nDataFrame dtypes after round trip:")
print(df_back.dtypes)