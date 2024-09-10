import unittest
from unittest import mock, TestCase
from unittest.mock import MagicMock


class test_class_A():
    def b(self):
        print("B")
        return False

    def a(self):
        ret = self.b()
        if ret:
            return True
        else:
            return False


class TestMock(TestCase):
    def test_function_A1(self):
        test = test_class_A()
        test.b = MagicMock(return_value=True)
        self.assertEqual(True, test.a())


if __name__ == '__main__':
    unittest.main()

# 动态地替换了 test_class_A 实例的 b 方法
test = test_class_A()
test.b = test_class_A().b
print(test.a())

print("=====================================")

result1 = mock.Mock(name='mock名称')

print(result1)

mock_value1 = mock.Mock(return_value="返回值1")

print(mock_value1())

mock_value2 = mock.Mock(return_value="返回值2", side_effect=[1, 2, 3])

print(mock_value2())

print(mock_value2())

print(mock_value2())

print(f'xx' + 'zz')
