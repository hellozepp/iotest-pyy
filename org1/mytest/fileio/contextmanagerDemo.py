from contextlib import contextmanager
import logging

logger = logging.getLogger(__name__)
connection_name = "myadapter"


class ConnectionHandler:
    # contextmanager 装饰器用于定义上下文管理器， 该装饰器的函数必须返回一个生成器
    # 使用注解后不用通过类的实例化来调用方法然后再next()来调用生成器，而是使用with语句来调用生成器，只需将 yield 包裹在 try 块中，这样更加简洁
    # yield 之前的代码在 __enter__ 方法中执行，yield 之后的代码在 __exit__ 方法中执行
    @contextmanager
    def exception_handler(self, sql: str):
        try:
            yield
        except ValueError as exc:
            self.release(connection_name)
            print('myadapter error: {}'.format(str(exc)))
            raise ValueError(str(exc))
        except Exception as exc:
            print("Error running SQL: {}".format(sql))
            print("Rolling back transaction.")
            self.release(connection_name)
            raise Exception(str(exc))

    def release(self, connection_name):
        # 释放连接的逻辑
        print("release connection: {}".format(connection_name))
        pass


# 使用示例
handler = ConnectionHandler()


def execute_some_sql_function():
    print("---execute_some_sql_function----")
    raise ValueError("test ValueError")


try:
    with handler.exception_handler("SELECT * FROM my_table"):
        # 在这个上下文中执行的代码
        execute_some_sql_function()
except ValueError as db_exc:
    # 处理数据库异常
    print("we found Database exception:", db_exc)
except Exception as rt_exc:
    # 处理运行时异常
    print("we found Runtime exception:", rt_exc)
