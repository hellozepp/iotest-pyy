from typing import TypeVar, Generic

T = TypeVar('T')


class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value


# 使用示例
int_container = Container[int](42)
print(int_container.get_value())  # 输出: 42

str_container = Container[str]("Hello")
print(str_container.get_value())  # 输出: Hello
