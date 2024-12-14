import os
import sys

from trans import test_parse_one

if __name__ == '__main__':
    # sys.argv = ['parse', 'last/reason_0/acid_insert_overwrite.q.sql']
    if not sys.argv or '.sql' not in sys.argv[0]:
        sys.argv = ['test.sql']
    dir = os.path.dirname(__file__)
    if len(sys.argv) < 1:
        print('Usage: argv[0] = sql_file_path')
        sys.exit(1)

    file_name = sys.argv[0]
    try:
        test_parse_one(os.path.join(dir, file_name), read='presto', dialect='clickzetta')
        bool = True
        if bool:
            sys.exit(0)
    except Exception as ex:
        print(f'Failed to parse {file_name}, reason: {ex}\n')
        bool = True
        if not bool:
            raise ex
        print(f'------{bool}--------')
        print('Does doris support the SQL?')
    try:
        test_parse_one(os.path.join(dir, file_name), read='doris', dialect='doris')
        bool = True
    except Exception as e1:
        print(f'Failed to parse {file_name}, reason: {e1}\n')
        print(f'------{bool}--------')
        print('Does snowflake support the SQL?')
    try:
        test_parse_one(os.path.join(dir, file_name), read='snowflake', dialect='snowflake')
        bool = True
    except Exception as e2:
        print(f'Failed to parse {file_name}, reason: {e2}\n')
        print(f'------{bool}--------')
    try:
        print('Does bigquery support the SQL?')
        test_parse_one(os.path.join(dir, file_name), read='bigquery', dialect='bigquery')
        bool = True
    except Exception as e3:
        print(f'Failed to parse {file_name}, reason: {e3}\n')
        print(f'------{bool}--------')
    try:
        print('Does spark support the SQL?')
        test_parse_one(os.path.join(dir, file_name), read='spark', dialect='spark')
        bool = True
    except Exception as e3:
        print(f'Failed to parse {file_name}, reason: {e3}\n')
        print(f'------{bool}--------')
    try:
        print('Does duckdb the SQL?')
        test_parse_one(os.path.join(dir, file_name), read='duckdb', dialect='duckdb')
        bool = True
    except Exception as e3:
        print(f'Failed to parse {file_name}, reason: {e3}\n')
        print(f'------{bool}--------')
    try:
        print('Does drill the SQL?')
        test_parse_one(os.path.join(dir, file_name), read='drill', dialect='drill')
        bool = True
    except Exception as e3:
        print(f'Failed to parse {file_name}, reason: {e3}\n')
        print(f'------{bool}--------')
    try:
        print('Does starrocks support the SQL?')
        test_parse_one(os.path.join(dir, file_name), read='starrocks', dialect='starrocks')
        bool = True
    except Exception as e3:
        print(f'Failed to parse {file_name}, reason: {e3}\n')
        print(f'------{bool}--------')
    try:
        print('Does presto support the SQL?')
        test_parse_one(os.path.join(dir, file_name), read='presto',
                       dialect='presto')
        bool = True
    except Exception as e3:
        print(f'Failed to parse {file_name}, reason: {e3}\n')
        print(f'------{bool}--------')
        raise e3
