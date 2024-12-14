import os
import sys
from datetime import datetime

from clickzetta.connector.v0.utils import split_sql

import sqlglot


def test_transpile_sql(file_path, read='doris', dialect='spark', pretty=True):
    if not os.path.exists(file_path):
        print(f'File {file_path} does not exist.')
        return

    with open(file_path, 'r') as f:
        content = f.read()

    sqls = split_sql(content)
    for i, sql in enumerate(sqls, start=1):
        sql = sql.strip()
        print(f'{read} SQL {i} as following:\n```\n{sql}\n```\n')
        if not sql:
            continue
        try:
            sqlglot.pretty = pretty
            # Dialect.get_or_raise(dialect).tokenizer_class.STRING_ESCAPES = ["'"]
            transpiled_sql = "\n;".join(sqlglot.transpile(sql, read=read, write=dialect)).strip()
            import psutil
            print("当前进程占用内存：", psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024, "MB")
            print(f'Transpiled to {dialect} sql to output :\n```\n{transpiled_sql}\n```\n')
        except Exception as ex:
            print(f'Failed to transpile SQL {i}, reason: {ex}\n')
            raise ex


def test_parse_one(file_path, read='hive', dialect='zettapark'):
    if not os.path.exists(file_path):
        print(f'File {file_path} does not exist.')
        return

    with open(file_path, 'r') as f:
        content = f.read()

    sqls = split_sql(content)
    del content
    for i, sql in enumerate(sqls, start=1):
        sql = sql.strip()
        if not sql:
            continue
        try:
            print(f'Parsing {read} SQL {i}:\n{sql}\n')
            sqlglot.pretty = False
            parsed_sql = sqlglot.parse_one(sql, read=read, dialect=dialect)
            print(f'Parsed {read} SQL {i}:\n{repr(parsed_sql)}\n')
        except Exception as ex:
            print(f'Failed to parse {read} SQL {i}, reason: {ex}\n')
            raise ex


if __name__ == '__main__':
    # sys.argv = ['parse', 'last/reason_0/acid_insert_overwrite.q.sql']
    if not sys.argv or '.sql' not in sys.argv[0]:
        sys.argv = ['test.sql']
    dir = os.path.dirname(__file__)
    if len(sys.argv) < 1:
        print('Usage: argv[0] = sql_file_path')
        sys.exit(1)

    read = 'presto'
    file_name = sys.argv[0]
    bool = False
    try:
        print(f"start time:{datetime.now()}")
        test_transpile_sql(os.path.join(dir, sys.argv[0]), read=read, dialect='clickzetta', pretty=False)
        print(f'end time {datetime.now()}')
        print("----------------------parse sql----------------------")
        test_parse_one(os.path.join(dir, file_name), read=read, dialect='clickzetta')
        bool = True
        if bool:
            exit(0)
    except Exception as ex:
        print(f'Failed to parse {file_name}, reason: {ex}\n')
        bool = True
        if bool:
            raise ex
        print(f'------{bool}--------')
    print('Does hive support the SQL?')
    try:
        test_transpile_sql(os.path.join(dir, file_name), read=read, dialect='hive')
        bool = True
    except Exception as e1:
        print(f'Failed to parse {file_name}, reason: {e1}\n')
        print(f'------{bool}--------')
    print('Does doris support the SQL?')
    try:
        test_transpile_sql(os.path.join(dir, file_name), read=read, dialect='doris')
        bool = True
    except Exception as e1:
        print(f'Failed to parse {file_name}, reason: {e1}\n')
        print(f'------{bool}--------')
    print('Does snowflake support the SQL?')
    try:
        test_transpile_sql(os.path.join(dir, file_name), read=read, dialect='snowflake')
        bool = True
    except Exception as e2:
        print(f'Failed to parse {file_name}, reason: {e2}\n')
        print(f'------{bool}--------')

    print('Does bigquery support the SQL?')
    try:
        test_transpile_sql(os.path.join(dir, file_name), read=read, dialect='bigquery')
        bool = True
    except Exception as e3:
        print(f'Failed to parse {file_name}, reason: {e3}\n')
        print(f'------{bool}--------')
    print('Does spark support the SQL?')
    try:
        test_transpile_sql(os.path.join(dir, file_name), read=read, dialect='spark')
        bool = True
    except Exception as e3:
        print(f'Failed to parse {file_name}, reason: {e3}\n')
        print(f'------{bool}--------')
    print('Does duckdb the SQL?')
    try:
        test_transpile_sql(os.path.join(dir, file_name), read=read, dialect='duckdb')
        bool = True
    except Exception as e3:
        print(f'Failed to parse {file_name}, reason: {e3}\n')
        print(f'------{bool}--------')
    print('Does drill the SQL?')
    try:
        test_transpile_sql(os.path.join(dir, file_name), read=read, dialect='drill')
        bool = True
    except Exception as e3:
        print(f'Failed to parse {file_name}, reason: {e3}\n')
        print(f'------{bool}--------')
    print('Does starrocks support the SQL?')
    try:
        test_transpile_sql(os.path.join(dir, file_name), read=read,
                           dialect='starrocks')
        bool = True
    except Exception as e3:
        print(f'Failed to parse {file_name}, reason: {e3}\n')
        print(f'------{bool}--------')
    print('Does presto support the SQL?')
    try:
        test_transpile_sql(os.path.join(dir, file_name), read=read,
                           dialect='presto')
        bool = True
    except Exception as e3:
        print(f'Failed to parse {file_name}, reason: {e3}\n')
        print(f'------{bool}--------')
        raise e3
    print('Does postgres support the SQL?')
    try:
        test_transpile_sql(os.path.join(dir, file_name), read=read,
                           dialect='postgres')
        bool = True
    except Exception as e3:
        print(f'Failed to parse {file_name}, reason: {e3}\n')
        print(f'------{bool}--------')
        raise e3
